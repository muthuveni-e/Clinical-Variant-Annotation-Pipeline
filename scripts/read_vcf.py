vcf_file="data/sample.vcf"
try:
    with open(vcf_file,"r")as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("VCF file not found!")