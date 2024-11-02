# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = [] #List to hold candidate names
candidateVotes = {} #dictionary to hold the votes each candidate receives

# Winning Candidate and Winning Count Tracker
winningCount = 0
winningCandidate = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        if row[2] not in candidates:

        # If the candidate is not already in the candidate list, add them
            candidates.append(row[2])

        # Add a vote to the candidate's count
        #{"key":value}
        #start the counter at 1
            candidateVotes [row[2]]=1
    
        else:
            candidateVotes [row[2]]+=1


vote_output = ""
for Candidate in candidateVotes:
    votes=candidateVotes.get(Candidate)
    votePct = float(votes)/ float(total_votes) *100.00

    vote_output += f"\t{Candidate}: {votePct:.2f}% Total: ({total_votes})\n\n"

    if votes>winningCount:
        #update the votes to the new winning count
        winningCount = votes
        #update the winning candidate
        winningCandidate = Candidate    

#generate output
winningCandidateOutput = f"Winner: {winningCandidate}\n"

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Generate and print the winning candidate summary
    output = (
        f"\n\nElection Results\n\n"
        f"--------------------------------\n"
        f"\nTotal Votes: {total_votes:,}\n\n"
        f"--------------------------------\n"
        f"\n{vote_output}\n"
        f"--------------------------------\n"
        f"\n{winningCandidateOutput}\n"
        f"--------------------------------\n"

    )

    print(output)

    # Save the winning candidate summary to the text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)