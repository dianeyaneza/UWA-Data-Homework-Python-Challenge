import os 
import csv 

# Import the csv file
election_csv = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')

# Set initial variables
votes_cast = 0
candidates = {}
khan = []
correy = []
li = []
otooley = []
row_count = 0
winner_count = 0

# Open and read the csv file to find the requirements 
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read after the header row
    header = next(csvreader)

    # Read rows  
    for row in csvreader:

        # Find the total number of votes cast
        votes_cast += 1

        # Show a complete list of candidates who received votes
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # Set conditionals to determine the number of votes cast per candidate
        if (row[2]) == "Khan":
            khan.append(row[2])
        elif (row[2]) == "Correy":
            correy.append(row[2])
        elif (row[2]) == "Li":
            li.append(row[2])
        elif (row[2]) == "O'Tooley":
            otooley.append(row[2])

        # Find the vote percentages of each candidate
        per_khan = round(float((len(khan)) / votes_cast * 100),2)
        per_correy = round(float((len(correy)) / votes_cast * 100),2)
        per_li = round(float((len(li)) / votes_cast * 100),2)
        per_otooley = round(float((len(otooley)) / votes_cast * 100),2)

    # Determine the winner based on who has the highest number of votes 
    for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]
  
    # print("Election Results")
    # print("------------------------")
    # # Print out the total votes cast
    # print(f"Total Votes: {str(votes_cast)}")
    # print("------------------------")
    # # Print out the votes cats per candidate
    # print(f"Khan: {str(per_khan)}% ({str(len(khan))})")
    # print(f"Correy: {str(per_correy)}% ({str(len(correy))})")
    # print(f"Li: {str(per_li)}% ({str(len(li))})")
    # print(f"O'Tooley: {str(per_otooley)}% ({str(len(otooley))})")
    # print("------------------------")
    # print(f"Winner: {str(winner)}")
    # print("------------------------")

# Define election results data
file_data = f'''
Election Results
------------------------
Total Votes: {str(votes_cast)}
------------------------
Khan: {str(per_khan)}% ({str(len(khan))})
Correy: {str(per_correy)}% ({str(len(correy))})
Li: {str(per_li)}% ({str(len(li))})
O'Tooley: {str(per_otooley)}% ({str(len(otooley))})
------------------------
Winner: {str(winner)}
------------------------
'''

# Print data to the terminal
print(file_data)

# Specify financial analysis data output file and location
data_output = os.path.join("Analysis","PyPoll_Election_Results.txt")

# Write data as a text file
with open(data_output, "w") as txtfile:
    txtfile.write(file_data)