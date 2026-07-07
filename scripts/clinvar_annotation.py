import csv

clinvar = {}

with open("data/clinvar_database.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        clinvar[row["Position"]] = row["Clinical_Significance"]

print("ClinVar Annotation")

with open("data/sample.vcf", "r") as vcf:

    for line in vcf:

        if line.startswith("#"):
            continue

        columns = line.strip().split()

        position = columns[1]

        significance = clinvar.get(position, "Not Found")

        print("--------------------")
        print("Position:", position)
        print("Clinical Significance:", significance)