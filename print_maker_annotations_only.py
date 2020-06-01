import gzip

switch=0
for line in open("CtarK1_sorted.gff3"):
    if line[:2]=="##" and len(line.strip())>3:  # headers
        print(line.strip())
        continue
    if line.strip()=="###" and switch==0:  # spacers
        switch=1
        print(line.strip())
        continue
    if line.strip()=="###" and switch==1:  # spacers
        continue
    if line.strip().split()[1] == "maker" or line.strip().split()[1] == "Geneious":
        print(line.strip())
        switch=0
