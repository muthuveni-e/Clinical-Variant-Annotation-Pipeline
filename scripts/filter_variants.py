import csv

freq_dict = {}

with open("data/population_frequency.csv", "r") as freq_file:

    reader = csv.DictReader(freq_file)
    print(reader.fieldnames)

    for row in reader:
        freq_dict[row["Position"]] = float(row["Frequency"])

print("Rare Variants")

with open("data/sample.vcf", "r") as vcf_file:

    for line in vcf_file:

        if line.startswith("#"):
            continue

        columns = line.split()

        position = columns[1]

        frequency = freq_dict.get(position, None)
        

        if frequency < 0.01:

            print("-------------------")

            print("\nRare Variant Found" )
            print("Position:",position)
            print("Frequency:",frequency)

            print("-------------------")