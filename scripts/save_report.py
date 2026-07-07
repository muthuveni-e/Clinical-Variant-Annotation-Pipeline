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
            "Effect": row["Effect"],
            "Disease": row["Disease"]
        }

# Create report file
with open("results/clinical_report.csv", "w", newline="") as report_file:

    writer = csv.writer(report_file)

    writer.writerow([
        "Position",
        "Gene",
        "Effect",
        "Disease",
        "Frequency",
        "Score",
        "Priority"
    ])

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
                disease = annotation_dict[position]["Disease"]

                score = 1

                if effect == "Missense":
                    score += 1

                if effect == "Nonsense":
                    score += 2

                priority = "HIGH" if score >= 3 else "MODERATE"

                writer.writerow([
                    position,
                    gene,
                    effect,
                    disease,
                    frequency,
                    score,
                    priority
                ])

print("Clinical report saved successfully!")