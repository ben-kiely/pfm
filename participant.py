# Ben Kiely 122361921 Assignment 1: The Iowa Gambling Task.
'''
19.5 / 25

Well done, Ben. I have some comments for you to review below.

Classes
The student has modified the methods in the TrialParticipant class to allow for reuse to some extent, however, there is still some hardcoded variables not explained (see comments). The student adds the additional methods and works well. 
A small number of methods not working as described (see below).
Comments are great.

Main code
An instance of the TrialParticipant class is created. The student references the TrialParticipant class to create all experiment interactions described.
There are some issues with the code affecting the flow of the program – see below.
Great use of comments. 
'''
### ---- TRIALPARTICIPANT CLASS ----------
class TrialParticipant:

    #class variables
    instances_of_participants = 0
    decks = { 
        1: {
            'A': [100, 0], # make sure these are ints
            'B': [250, 0], 
            'C': [50, 0], 
            'D': [50, 0]
            }, 
        2: {
            'A': [0, 100], 
            'B': [0, 250], 
            'C': [0, 50], 
            'D': [50, 0]
            }, 
        3: {
            'A': [100, 50], 
            'B': [100, 0], 
            'C': [50, 0], 
            'D': [50, 0]
            }, 
        4: {
            'A': [100, 0], 
            'B': [100, 0], 
            'C': [50, 0], 
            'D': [50, 0]
            }
        }

    def __init__(self, fname, lname):
        #Question A // First Name
        self.first_name = fname
        #Question A // Last Name
        self.last_name = lname
        #Question A // Variable counting how many instances of the class is created
        TrialParticipant.instances_of_participants += 1
        #Question A // Counting how many participants are taking part
        self.participant_num = TrialParticipant.instances_of_participants
        #Question A // Made the winnings a private variable, source: CS2011-PrivateVariables-LectureNotes.pdf
        self.__winnings = 2000
        #Question A // Private dictionary containing which keys participants have pressed and how many times
        self.__keyspressed = {"a": 0, "b": 0, "c": 0, "d": 0}
        #Question A // The amount of times the position is incremented after each key pressed
        self.position = 1
    #Question B // Created a string representation, used object information sentence from slides, source: CS2011-presenting-information.pdf. %s is a placeholder for string (first name and last name). %d is for integers (participant number). Slide 7 of previous source listed the formatters and examples(very helpful!). 
    def __str__(self):
        return "Object Information; Participant Name: %s %s, Participant Number: %d" % (self.first_name, self.last_name, self.participant_num)
    
    #Question K // Getters and Setters for Name, which will be tested at the end. Used the bank account example for help from slide 3, source: CS2011-GettersSetters-LectureNotes-revised.pdf
    def get_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    def set_name(self, fullname):
        fname, lname = fullname
        self.first_name = fname
        self.last_name = lname
    #Question C // This method assesses the win and lose amount from the associated deck from the round. There is a few things going on here. 1. I used 'strip' and 'upper' to get rid of trailing spaces and to account for lowercase user inputs to make them all capital. 2. The 'if' statement looks at the input deck key and sees if it exists in the deck dictionary above. 3. If it's found it returns win and lose amounts as a list (square brackets). Otherwise (else), it returns none. 
    def choose_deck(self, deck):
        deck = deck.strip().upper()
        if deck in self.decks[1]:
            return self.decks[1][deck]
        else:
            return None
    #Question D // This method takes the 2000 euro (self.__winnings a private variable) and uses the parameter 'win_lose' to calculate win loss amount and apply it to the participants overall winnings. Again, used square brackets to return a list.
    def update_bank(self, win_lose):
        winnings = self.__winnings
        newWinnings = winnings - win_lose[1]+win_lose[0]
        self.__winnings = newWinnings
        return newWinnings
    #Question E // Goal of this method is to see if the function returns the character presses made by the participant as a list of tuples. First, I created an empty list 'dictionarylist'. 
    def get_keypresses(self):
        dictionarylist = []
        keyspressed = self.__keyspressed # Here, the variable keyspressed is assigned the value of the private attribute __keypressed of the current instance of the class.
        for key, value in keyspressed.items(): # This line initiates a loop over the items (key-value pairs) in the keyspressed dictionary.
            temp = [key,value] # I didn't know how to make a temporary list(temp), so I googled it. I'm sure there's an easier way to do this but I was stuck. source: http://introtopython.org/lists_tuples.html#Lists-and-Looping
            dictionarylist.append(temp) # The temp list is appended to the dictionarylist list.
        return dictionarylist # The dictionarylist is returned, containing all the key-value pairs from the keyspressed dictionary in the form of a list of lists, where each sublist contains the key and value from the original dictionary.
    #Question F // Hard Coded this, resets deck position to 1.
    def reset(self):
        self.position = 1
    # Misc // Instructions and Consent
    def display_welcome(self):
        print("Welcome to the Iowa Gambling Task!")
    def display_instructions(self):
        print("The Iowa Gambling Task consists of four decks: A, B, C or D.")
        print("You start with €2000 in the bank and depending on which deck you choose your total will increase or decrease.")
    def display_consent(self):
        print("If you would like to play the game, hit A, B, C or D. If not, please hit Q.")
    
    #Question G // I left this code as is from the template, as it increments the position by 1 already and terminates after 4 rounds.
    def increment_position(self):
        self.position = self.position + 1
        if self.position > 4:
            return False
        return True
    
    def get_position(self):
        return self.position
    #Question H // This function counts how many times user clicks characters a, b, c or d. Method takes in two parametters, self and keyspressed. 
    def record_key(self, keyspressed):
        chardict = self.__keyspressed # chardict is local variable which references private attribute  __keyspressed in the current instance. Dictionary keeps track of how many times each character was selected.
        if keyspressed == "a" or keyspressed == "b" or keyspressed == "c" or keyspressed == "d": # checks if each value is equal to keyspressed. Ensures only specific keys a,b,c or is recorded, rest filtereed out.
            chardict[keyspressed] += 1 #if the conditions of 'if' value are met, this line increments the value of keyspressed in the chardict dictionary by 1.
    #Question I // #Goal is to find the most frequent keys pressed by user in Iowa Gambling Task.
    def most_frequent_keys(self): # declares the method most_frequent_keys within the class. The method doesn't take any additional arguments besiddes the usual self.
        highestkey = 0 #this variable will keep track of the highest keys pressed
        highestkeylist = [] #empty list that will store highest keys pressed
        dictionarylist = self.__keyspressed #dictionarylist references private attribute __keyspressed
        for item in dictionarylist.items(): #loop through each value pair in dictionarylist
            key = item[0] #extracts key and value pair in dictionarylist
            value = item[1] #''
            if value > highestkey: #checks if current value is higher than previous highest value.
                highestkey = value #if current value is higher than previous value, it will update to highestkey
                for k, v in dictionarylist.items(): #another loop through each key value pair to find highest keys with highest count in dictionarylist
                    if v == highestkey: #checks if value is equal to highest key
                        highestkeylist.append((k, v)) #if value is equal to highest key this line appends it into a tuple hence ().
        return highestkeylist #returns list of highest key value presses
    #Question J //Same as above formatting.
    def least_frequent_keys(self):
        lowestkey = 0
        lowestkeylist = []
        dictionarylist = self.__keyspressed
        for item in dictionarylist.items():
            key = item[0]
            value = item[1]
            if value < lowestkey:
                lowestkey = value
        for k, v in dictionarylist.items():
            if v == lowestkey:
                lowestkeylist.append((k, v))
        return lowestkeylist
    
    #Question K // Properties for Getter and setter 
    fullname = property(get_name, set_name)
    



    



#### ------- MAIN CODE ---------------

run_experiment = True
instructions = "Enter one of the following characters to choose your winning:\n\n---->A   B   C   D<----"

trial_participant = TrialParticipant("Ben", "Kiely")

while run_experiment:
    print("\n"*20)
    trial_participant.display_welcome()
    trial_participant.display_instructions()
    trial_participant.display_consent()
    
    position = trial_participant.get_position()
    print(f"Participant {trial_participant.participant_num} has €{trial_participant.update_bank([0, 0])} in the Bank")
    print("The deck position is: ", position)
    response = input(instructions + "\n")
    if response.lower() == "q":
        run_experiment = False
    else:
        deck_result = trial_participant.choose_deck(response)
        if deck_result:
            new_winnings = trial_participant.update_bank(deck_result)
            print(f"Participant {trial_participant.participant_num} has €{new_winnings} in the Bank")
        
    
    if response.lower() == "q":
        run_experiment = False
    else:
        next = trial_participant.increment_position()
        if next == False:
            run_experiment = False
print("Task has completed.")
print("Iowa task terminated.")

if __name__ == '__ Main__':

    # Creating instance of class
    p1 = TrialParticipant("Ben", "Kiely")

    

    #testing fullname Property
    p1.fullname = "Ben Kiely"
    print(p1.fullname)

    
