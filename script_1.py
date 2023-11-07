import os
from sequence_class import Seq

def readSARS_CoV2_FASTA():
    # Assumes that the FASTA file is in the same directory as the script
    # Also assumes that the file is named "SARS-CoV-2 RNA Genome FASTA.txt"
    with open("SARS-CoV-2 RNA Genome FASTA.txt", "r") as f:
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
    seq_0 = readSARS_CoV2_FASTA()
    # Print the contents of the sequence in seq_0
    print(seq_0.__str__()[0:-1])

if __name__ == "__main__":
    main()