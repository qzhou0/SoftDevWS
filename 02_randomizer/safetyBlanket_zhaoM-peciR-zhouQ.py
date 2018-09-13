#SafetyBlanket - Rubin Peci, Qian Zhao, Maggie Zhao
#SoftDev pd7
#K02: NO-body expects the Spanish Inquisition!
#2018-09-06

#need this import to pick a random choice
import random

#the dictionary given to us
KREWES = { 
'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'], 
'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'], 
'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']}

#function that picks a random entry in the dictionary, given the desired team
def pick_random(key):
    #gets the list associated with the key
    students = KREWES[key]
    #returns a random value from the list
    return random.choice(students)

#main method
def main():
    #gets the user choice on what team they want to pick from
    choice = input("Please pick a team from the choices (w, m, x): ")
    
    #tests if what they typed in is a valid option; if not, then it keeps repeating until something valid is inputted
    while choice not in KREWES.keys():
        print('Invalid option! Try again!')
        choice = input("Please pick a team from the choices (w, m, x): ")
    #prints the random member from the given team
    print("Random member from team " + choice + ": " + pick_random(choice))

main() #call to the main method