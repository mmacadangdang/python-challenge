import os
import csv

# Files to load
pypoll = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis", "election_data.txt")

# Variables needed
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Read the csv
with open(pypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header
    header = next(csvfile)

    # For each row...
    for row in csvreader:

        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] =  candidate_votes[candidate_name] + 1

# Print results to text file
with open(output_file, "w") as text_file:

    output = (
        f"Election Results\n "
        "------------------------------------- \n"
        f"Total Votes: {total_votes}\n"
        "------------------------------------- \n"
        )

    # Print results
    print(output)

    # Save the final vote count to the text file
    text_file.write(output)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage
        new_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n" 

        print(new_output, end="")

        # Save each candidate's voter count and percentage to text file
        text_file.write(new_output)

    # Print the winning candidate
    winner = winning_candidate
    print(winner)

    # Save the winning candidate's name to text file
    text_file.write(winner)
