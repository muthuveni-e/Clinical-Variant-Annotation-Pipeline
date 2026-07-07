vcf_file = "data/sample.vcf"

with open(vcf_file, "r") as file:
    for line in file:

        if line.startswith("#"):
            continue

        columns = line.split()

        chrom = columns[0]
        pos = columns[1]
        ref = columns[3]
        alt = columns[4]

        print("Chromosome:", chrom)
        print("Position:", pos)
        print("Reference:", ref)
        print("Alternative:", alt)
        print("------------------")
