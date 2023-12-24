import csv
import time

def readSARS_CoV2_FASTA():
    # Assumes that the FASTA file is in the same directory as the script
    # Also assumes that the file is named "SARS-CoV-2 RNA Genome FASTA.txt"
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
        return "".join(lines)

def main():
    threshold_limit = float(input("Input the threshold value from the previous script: "))
    start_time = time.time()
    sequence = readSARS_CoV2_FASTA()
    final_results = []
    for idx in range(len(sequence) - 49):
        g_count = sequence[idx:idx+50].count("G")
        if g_count > threshold_limit:
            final_results.append([idx + 1, g_count])
    final_results = sorted(final_results, key=lambda x: x[1], reverse=True)
    with open("top_5_g_enriched_regions.txt", "w", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["Name","Start", "End", "G-content"])
        for i in range(5):
            writer.writerow(["NC_045512.2", final_results[i][0], final_results[i][0]+49, final_results[i][1]])
    with open("all_g_enriched_regions.txt", "w", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["Name","Start", "End", "G-content"])
        for i in range(len(final_results)):
            writer.writerow(["NC_045512.2", final_results[i][0], final_results[i][0]+49, final_results[i][1]])
    end_time = time.time()
    print("Calculation is finished!")
    print("Time elapsed: {} seconds".format(end_time - start_time))

if __name__ == "__main__":
    main()

