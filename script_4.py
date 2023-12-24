import csv

def read_SARS_CoV_2_FASTA():
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
    # Read into "mutations.csv" file and retrieve only the fourth column
    # Reason being we only need the genomic locations of the mutations
    with open("mutations.csv", "r") as f:
        file_contents = f.readlines()
        locations = []
        for line in file_contents:
            locations.append(line.strip().split(",")[3])
    # Then, we read the FASTA format of the original SARS-CoV-2 sequence
    sequence = read_SARS_CoV_2_FASTA()
    # Setting the min and max value of the range so that we don't go out of bounds
    min_value = 0
    max_value = len(sequence)
    # For each genomic location in the "mutations.csv" file, named X
    # We create a range of [X - 25, X + 25] and count the G-population inside the range
    # Then, we append the count to a list named "final_results"
    #   in the format of [genomic_location, G-population]
    threshold = 14.665 # Hard-coded, change if needed
    final_results = []
    for elem in locations:
        elem = int(elem)
        count = 0
        min_range_val = elem - 25 if elem - 25 >= min_value else min_value
        max_range_val = elem + 25 if elem + 25 <= max_value else max_value
        g_count = sequence[min_range_val:max_range_val+1].count("G")
        final_results.append([elem, g_count, "Larger than threshold" if g_count > threshold else "Smaller than threshold"])
    final_results = sorted(final_results, key=lambda x: x[1], reverse=True)
    with open("top_10_g_enriched_regions_mutations.txt", "w", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["Name","Start", "End", "G-content", "Results"])
        for i in range(10):
            writer.writerow(["NC_045512.2", final_results[i][0], final_results[i][0]+49, final_results[i][1], final_results[i][2]])
    less_than_threshold = 0
    more_than_threshold = 0
    for result in final_results:
        if result[2] == "Smaller than threshold":
            less_than_threshold += 1
        else:
            more_than_threshold += 1
    print("Number of regions with G-content less than threshold: {} ({}% of total)"
          .format(less_than_threshold, (less_than_threshold/(less_than_threshold+more_than_threshold))*100))
    print("Number of regions with G-content more than threshold: {} ({}% of total)"
          .format(more_than_threshold, (more_than_threshold/(less_than_threshold+more_than_threshold))*100))

if __name__ == "__main__":
    main()