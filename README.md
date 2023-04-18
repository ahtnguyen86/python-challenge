# python-challenge
python-challenge

in PyPoll main.py
candidate_results = (f"{candidate}: {vote_percentage:0.3f}% ({votes:})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to text file.
        txt_file.write(candidate_results)

I referenced https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python to learn to round the percentage 3 decimal places "0.3f"        