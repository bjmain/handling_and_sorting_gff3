import glob
import os

# This script updates sample numbers so they can be sorted.

gffs = glob.glob("*gff3")

for f in gffs:
    num = f.split(".")[0].split("_")[1]
    name = f
    if len(num)==3:
        name = "chnk_" + "0" + num + ".gff3" 
    if len(num)==2:
        name = "chnk_" + "00" + num + ".gff3" 
    if len(num)==1:
        name = "chnk_" + "000" + num + ".gff3" 
    os.system("mv %s %s" % (f, name))
