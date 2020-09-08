# csv module is used to elegantly open the data file.
import csv
# random module is used to generate random numbers.
import random

# Method reads and returns the student data file with intra row separation through the "\t" delimiter.
# The index [1:] is used to skip past the first row which contains the attributes.
def retrieveData():
    return [entry for entry in csv.reader(open("../data/fall-20-students.tsv"), delimiter = "\t")][1:]

# Method gets and validates user input. While the character remains null, non-numeric, or negative
#the loop continues. Any positive numeric value passed in will be converted and returned as an integer.
def teamQtyInput():
    teamQtyValue = '\0'
    while (not(teamQtyValue.isnumeric())):
        teamQtyValue = (input("Please enter a positive and non-zero integer value for team quantity:"))
    return int(teamQtyValue)


# Method uses linear comprehension to create _teamQty amount of empty lists to prepare for population.
# While loop iterates until _studentList is empty, randomly selecting, without replacement, students
# to be placed into the teams list.
def setGroups(_studentList, _teamQty):
    teams = [[] for x in range(_teamQty)]
    while(_studentList != []):
        [teams[x].append(_studentList.pop(random.randrange(len(_studentList))))\
         for x in range (_teamQty) if len(_studentList) != 0]
    return teams

# Method first gets the list of teams by passing the student data and user input into method setGroups.
# Method then
def main():
    teams = setGroups(retrieveData(), teamQtyInput())
    print(str(["Team {} ({} Members) \n -------------- \n {} \n\n".\
                   format(x+1, len(teams[x]), teams[x]) for x in range(0, len(teams))]))
main()
