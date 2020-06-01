import glob
import os
import sys

gffs = sorted(glob.glob("chnk*gff3"))



header_D ={}
D = {}
for f in gffs:
    for line in open(f):
        if "FASTA" in line.strip():
            break
        if line[0]=="#":
            continue
        tig = line.strip().split()[0]
        if tig not in D:
            D[tig]=[]
        D[tig].append(line.strip()) #.strip().split())
        if line.strip().split()[2] == "contig":
            if line.strip().split()[2] not in header_D:
                header_D[line.strip()]=1

    
print "##gff-version 3"
print "##genome-build CtarK1" 
for header in sorted(header_D):
    h=header.split()
    print "##sequence-region", h[0], h[3], h[4]  # tig and size

for CONTIG in sorted(D):
    for row in D[CONTIG]:
        print row

