# This script aims to answer part 2 of Q1
# Please write a python script, which take input sequences from FASTA file (shuffled 1000
# sequences) and counts number of G in 50nt window there (G-content) by sliding it down with
# 1nt movement, stores the results (maybe dictionary data structure) and finds the values reaching
# more than top 5% of the G-content population. You have to provide both a python script and value
# of significant G-content (P<0.05), that will be used as cutoff for following question.

# File name of the FASTA file: output_script_1.txt
import numpy as np
import pandas as pd

def read_filename():
    # Read the file and return an array of the contents
    filename = "output_script_1.txt"
    with open(filename, "r") as f:
        file_contents = f.readlines()
        lines = []
        for line in file_contents:
            if line.startswith(">"):
                continue
            lines.append(line.strip())
        return lines

def main():
    # Steps on how this algorithm works:
    # 1. Read the file and store the contents in an array
    # 2. There are 1000 sequences now stored in the array, now we need to split each sequence into 50nt windows
    # 3. Count the number of Gs in each 50nt window
    # 4. Save the number of Gs in each 50nt window in a 2D array named temp_results
    # Structure of said array is [start index, percentage of Gs in 50nt window]
    # Sort the results, return the threshold of the top 5% of the G-content population
    # Repeat for all 1000 sequences, store in a 2D array named final_results with the structure of [sequence number, threshold of the top 5% of the G-content population]
    # Return the average of the top 5% of the G-content population from all 1000 sequences
    sequences = read_filename()
    final_results = []
    for i in range(len(sequences)):
        temp_results = []
        for j in range(len(sequences[i])-49):
            temp_results.append([j, sequences[i][j:j+50].count("G")])
        temp_results = sorted(temp_results, key=lambda x: x[1])
        threshold = temp_results[int(len(temp_results)*0.95)][1]
        final_results.append([i+1, threshold])
    threshold = sum([i[1] for i in final_results])/len(final_results)
    print("Threshold for G-enrich regions in a 50 nucleotide window is {}".format(threshold))
    print("Calculation is finished!")
    # The threshold is 14.659 with current random seed of 1000 sequences
        
        
if __name__ == "__main__":
    main()