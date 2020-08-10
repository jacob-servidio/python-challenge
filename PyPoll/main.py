#import
import os
import csv

#variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes =0
otooley_votes = 0

#path for csv
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    #calc total votes
    for row in csvreader:
        total_votes += 1

        #calc total votes for each canidate
        if (row[2]== "Khan"):
            khan_votes += 1
        elif (row[2]== "Correy"):
            correy_votes +=1
        elif (row[2]== "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
    
    #calc percentage for each candidate
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

    #calc winner
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'tooley"


#print in terminal
print(f"Election Results")
print(f"---------------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------------")
print(f"Kahn: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------------")
print(f"WINNER: {winner_name}")
print(f"---------------------------------")
