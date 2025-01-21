more Code/MCB185/data/A.thaliana.gff | cut -f 7 | grep [+-] | sort | uniq -cut
more Code/MCB185/data/GBF_Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gbff | cut -f 2 | grep "kinase" | sort | uniq -c
more Code/MCB185/data/GBF_Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gbff | cut -f 2 | grep "isomerase" | sort | uniq -c