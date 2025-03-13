import sys
import gzip
import mcb185 # type: ignore

fastas_file = sys.argv[1]

fastas = mcb185.read_fasta(fastas_file)

in_gene = False
pstrand = False

source = 'Genbank'
seqtype = 'gene'

for defline, fasta in fastas:
    sidx = 0
    eidx = 0
    i = 0
    jump = 1
    while i in range(len(fasta)):
        if fasta[i:i+3] == 'ATG' and not in_gene:
            in_gene = True
            sidx = i
            jump = 3
        if fasta[i:i+3] == ('TGA' or 'TGG' or 'TAG') and in_gene == True:
            in_gene = False
            eidx = i
            if pstrand:
                strand = '+'
            else:
                strand = '-'
            phase = i % 3
            id = 'geneid'
            name = 'genename'
            print(defline.split()[0],'\t',
                source,'\t',
                seqtype,'\t',
                sidx,'\t',
                eidx,'\t',
                '.','\t',
                strand,'\t',
                phase,'\t',
                'ID=',id,';','Name=',name,sep='')
            jump = 1
        i += jump