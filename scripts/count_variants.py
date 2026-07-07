vcf_file = "data/sample.vcf"
variant_count = 0
with open(vcf_file,"r") as file:
    for line in file:
        
        if line.startswith("#"):
            continue

        variant_count += 1
print("Total variants:",variant_count)