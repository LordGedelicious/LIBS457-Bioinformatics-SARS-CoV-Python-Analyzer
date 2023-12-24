import os
import time
import random
from sequence_class import Seq

def readSARS_CoV2_FASTA():
    # Assumes that the FASTA file is in the same directory as the script
    # Also assumes that the file is named "sequence.fasta"
    with open("sequence.fasta", "r") as f:
        # Read the file and store the contents in a variable
        file_contents = f.readlines()
        lines = []
        for line in file_contents:
            # Skip the lines that start with ">" or lines that doesn't start with "A", "G", "T", or "C"
            if line.startswith(">") or not line.startswith(("A", "G", "T", "C")):
                continue
            # Print the lines of the file
            lines.append(line.strip())
        # Create initial Seq object
        seq = Seq(0, "".join(lines))
        return seq

def main():
    start_time = time.time()
    seq_0 = readSARS_CoV2_FASTA()
    # Create 1000 shuffled sequences in FASTA format
    for i in range(0, 1000):
        # Creates a new Seq object with the shuffled sequence
        seq = Seq(i+1, ''.join(random.sample(seq_0.get_str(), len(seq_0.get_str()))))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        # Write the FASTA format to a file
        with open("output_script_1.txt", "a") as f:
            f.write(seq.return_fasta_format())
    end_time = time.time()
    print("Done!")
    print("Time elapsed: " + str(end_time - start_time) + " seconds")

if __name__ == "__main__":
    main()