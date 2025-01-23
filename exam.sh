gunzip -c Code/MCB185/data/A.thaliana.gff.gz | cut -f 7 | grep [+-] | sort | uniq -c
gunzip -c Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gbff.gz | cut -f 3 | grep "kinase" | wc
gunzip -c Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gbff.gz | cut -f 3 | grep "isomerase" | wc