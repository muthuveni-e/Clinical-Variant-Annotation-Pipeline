import csv

freq_dict = {}
annotation_dict = {}

# Read frequency database
with open("data/population_frequency.csv", "r") as freq_file:

    reader = csv.DictReader(freq_file)

    for row in reader:

        freq_dict[row["Position"]] = float(row["Frequency"])

# Read annotation database
with open("data/annotation_database.csv", "r") as annotation_file:

    reader = csv.DictReader(annotation_file)

    for row in reader:

        annotation_dict[row["Position"]] = {
            "Gene": row["Gene"],
            "Effect": row["Effect"]
        }

print("\nCLINICAL VARIANT REPORT\n")

variant_count = 1

with open("data/sample.vcf", "r") as vcf_file:

    for line in vcf_file:

        if line.startswith("#"):
            continue

        columns = line.split()

        position = columns[1]

        frequency = freq_dict.get(position, 1)

        if frequency < 0.01:

            gene = annotation_dict[position]["Gene"]
            effect = annotation_dict[position]["Effect"]

            print("========================")
            print("Variant :", variant_count)
            print("Position:", position)
            print("Gene    :", gene)
            print("Effect  :", effect)
            print("Freq    :", frequency)
            print("========================")

            variant_count += 1