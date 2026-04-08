# --- Simple Voting System Project ---
# This script tracks votes for two candidates: Hagi and Hadas.
# I used a while loop to keep the system running until the user types 'SOF'.

hagi_votes = 0
hadas_votes = 0

# Start of the voting process
voter_name = input("Enter your name (or 'SOF' to finish): ")

while voter_name != "SOF":
    print("Candidates: 1 for Hagi, 2 for Hadas")
    
    # Getting the vote from the user
    user_input = input("Enter your vote: ")
    
    # Using if-elif to count the votes
    if user_input == "1":
        hagi_votes = hagi_votes + 1
        print("Vote added to Hagi.")
    elif user_input == "2":
        hadas_votes = hadas_votes + 1
        print("Vote added to Hadas.")
    else:
        print("Invalid vote, please try again.")

    # Ask for the next name to continue or stop the loop
    voter_name = input("\nEnter next name (or 'SOF' to finish): ")

# --- Printing the final results ---
print("\n--- Final Results ---")
print(f"Hagi total votes: {hagi_votes}")
print(f"Hadas total votes: {hadas_votes}")

# Checking who is the winner
if hagi_votes > hadas_votes:
    print("The winner is: Hagi!")
elif hadas_votes > hagi_votes:
    print("The winner is: Hadas!")
else:
    print("It's a tie (Teko)!")
