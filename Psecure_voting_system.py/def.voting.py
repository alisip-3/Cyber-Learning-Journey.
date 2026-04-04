def run_voting_system():
    """
    A professional voting management system that tracks votes
    between two candidates until a stop command is issued.
    """

    # Initialize vote counters
    candidate_a_votes = 0
    candidate_b_votes = 0

    print("--- Secure Digital Voting System ---")
    print("Type 'FINISH' as the name to stop the process and see results.\n")

    while True:
        voter_name = input("Enter Voter Name: ").strip().upper()

        # Exit condition
        if voter_name == "FINISH":
            break

        try:
            # Getting the vote and ensuring it's a valid number
            vote = int(input("Enter your vote (1 for Candidate A / 2 for Candidate B): "))

            if vote == 1:
                candidate_a_votes += 1
                print(f"Vote recorded for Candidate A.")
            elif vote == 2:
                candidate_b_votes += 1
                print(f"Vote recorded for Candidate B.")
            else:
                print("Invalid selection. Please choose 1 or 2.")

        except ValueError:
            print("Error: Please enter a numeric value for the vote.")

        print("-" * 20)

    # Displaying Final Results
    print("\n--- Final Election Results ---")
    print(f"Candidate A: {candidate_a_votes} votes")
    print(f"Candidate B: {candidate_b_votes} votes")

    if candidate_a_votes > candidate_b_votes:
        print("Outcome: Candidate A is the winner!")
    elif candidate_b_votes > candidate_a_votes:
        print("Outcome: Candidate B is the winner!")
    else:
        print("Outcome: The election ended in a tie (Teko).")


if __name__ == "__main__":
    run_voting_system()