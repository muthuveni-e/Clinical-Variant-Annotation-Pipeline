vcf_file = "data/sample.vcf"

variant_number = 1

with open(vcf_file, "r") as file:
    for line in file:

        if line.startswith("#"):
            continue

        columns = line.split()

        chrom = columns[0]
        pos = columns[1]
        ref = columns[3]
        alt = columns[4]

        print("Variant", variant_number)
        print("Chromosome:", chrom)
        print("Position:", pos)
        print("Mutation:", ref, "->", alt)
        print("------------------------")

        variant_number += 1
        