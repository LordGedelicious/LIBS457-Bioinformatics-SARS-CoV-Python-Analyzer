import time

def read_output_script_1():
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
    # 2. There are 1000 sequences now stored in the array, now we need to split 
    #    each sequence into 50nt windows
    # 3. Count the number of Gs in each 50nt window
    # 4. Save the number of Gs in each 50nt window in a 2D array named temp_results
    # Structure of said array is [start index, percentage of Gs in 50nt window]
    # Sort the results, return the threshold of the top 5% of the G-content population
    # Repeat for all 1000 sequences, store in a 2D array named final_results with the 
    #    structure of [sequence number, threshold of the top 5% of the G-content population]
    # Return the average of the top 5% of the G-content population from all 1000 sequences
    start_time = time.time()
    sequences = read_output_script_1()
    final_results = []
    for i in range(len(sequences)):
        temp_results = []
        for j in range(len(sequences[i])-49):
            temp_results.append([j, sequences[i][j:j+50].count("G")])
        temp_results = sorted(temp_results, key=lambda x: x[1])
        threshold = temp_results[int(len(temp_results)*0.95)][1]
        final_results.append([i+1, threshold])
    threshold = sum([i[1] for i in final_results])/len(final_results)
    end_time = time.time()
    print("Threshold for G-enrich regions in a 50 nucleotide window is {}".format(threshold))
    print("Calculation is finished!")
    print("Time elapsed: {} seconds".format(end_time - start_time))
    # The threshold is 14.665 with current random seed of 1000 sequences
        
        
if __name__ == "__main__":
    main()