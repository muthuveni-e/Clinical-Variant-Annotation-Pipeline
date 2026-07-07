import csv

annotation_dict = {}

with open("data/annotation_database.csv", "r") as annotation_file:

    reader = csv.DictReader(annotation_file)

    for row in reader:

        annotation_dict[row["Position"]] = {
            "Gene": row["Gene"],
            "Effect": row["Effect"]
        }

print("Annotated Rare Variants\n")

with open("data/sample.vcf", "r") as vcf_file:

    for line in vcf_file:

        if line.startswith("#"):
            continue

        columns = line.split()

        position = columns[1]

        if position in annotation_dict:

            gene = annotation_dict[position]["Gene"]
            effect = annotation_dict[position]["Effect"]

            print("------------------------")
            print("Position :", position)
            print("Gene     :", gene)
            print("Effect   :", effect)
            print("------------------------")
