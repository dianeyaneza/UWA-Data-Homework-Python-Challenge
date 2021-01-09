import os 
import csv 

# Import the csv file
election_csv = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')

# Set initial variables
votes_cast = 0
khan = 0
correy = 0
li = 0
otooley = 0

row_count = 0

# Open and read the csv file to find the requirements 
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read after the header row
    header = next(csvreader)

    # Read rows         
    for index, row in enumerate(csvreader):
        
        # Find the total votes cast
        votes_cast += 1

        if index == "Khan":
            khan = float(row[1])
        elif index == "Corey":
            correy = float(row[1])
        elif index == "Li":
            li = float(row[1])
        elif index == "O'Tooley":
            otooley = float(row[1])

        
    

    print("Election Results")
    print("---------------------------------------------------")
    # Print out the total votes cast
    print(f"Total Votes: {str(votes_cast)}")
    # Print out the votes cats per candidate
    print(f"Khan: {str(khan)}")

    