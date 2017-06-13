# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

"""listoflists = [["Rafael", 23], ["Isa", 25]]
my_list = ["Arsenal", 50, 30]

listoflists.append(my_list)


print (listoflists[0][0])"""

def read_data(filename):
    
    f = open(filename, "r").read()

    big_list = []
    for lines in f.split("\n"):
        my_list = lines.split(",")
        big_list.append(my_list)

    return (big_list)


def get_index_with_min_abs_score_difference(goals):
    for_index = goals[0].index("Goals")
    against_index = goals[0].index("Goals Allowed")
    max_diff = 10000000000
    for index, team_list in enumerate(goals):
        if(team_list[for_index] != "Goals"):
            abs_diff = abs(int(team_list[for_index]) - int(team_list[against_index]))
            #print ( abs_diff, index)
            if abs_diff < max_diff:
                #print ("ENTER",team_list)
                max_diff = abs_diff
                max_diff_index = index

    return max_diff_index

def get_team(index_value, parsed_data):
    team_index = parsed_data[0].index("Team")
    return (parsed_data[index_value][team_index])

    
footballTable = read_data("football.csv")
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))
