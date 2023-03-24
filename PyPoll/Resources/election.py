import csv
import os

# Define the path to the CSV file
csvpath = "election_data.csv"

# Create empty lists to store the data
voter_ids = []
counties = []
candidates = []

# Read in the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    next(csvreader)
    # Loop through each row and append the data to the appropriate list
    for row in csvreader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

# Calculate the total number of votes cast
total_votes = len(voter_ids)

# Create a set of unique candidates
unique_candidates = set(candidates)

# Create a dictionary to store the vote counts for each candidate
vote_counts = {}
for candidate in unique_candidates:
    vote_counts[candidate] = 0

# Count the number of votes each candidate received
for candidate in candidates:
    vote_counts[candidate] += 1

# Calculate the percentage of votes each candidate received
vote_percentages = {}
for candidate in vote_counts:
    vote_percentages[candidate] = (vote_counts[candidate] / total_votes) * 100

# Find the winner of the election
winner = max(vote_counts, key=vote_counts.get)

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in vote_counts:
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in vote_counts:
        txtfile.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")