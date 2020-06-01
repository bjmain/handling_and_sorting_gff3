#!/bin/bash

# options for sbatch
#SBATCH --nodes=1
#SBATCH --time=6800
#SBATCH --mem=20G # Memory pool for all cores (see also --mem-per-cpu)
#SBATCH --partition=bml
#SBATCH --job-name="sort_gff3"

# for calculating the amount of time the job takes
begin=`date +%s`
echo $HOSTNAME


# loading modules
module load genometools

# running commands
cd /home/yourpath/gff_files
gt gff3 -sort yes -tidy yes -gzip yes -o CtarK1_sorted.gff3.gz -v yes -force yes CtarK1_unsorted_untidy.gff3

# finished commands

# getting end time to calculate time elapsed
end=`date +%s`
elapsed=`expr $end - $begin`
echo Time taken: $elapsed

