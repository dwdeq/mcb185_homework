def transcribe(dna):
    return dna.replace('T','U') # replaces all Ts with Us

def revcomp(dna):
    rc = []
    for nt in dna[::-1]:
        if   nt == 'A': rc.append('T') # adds a T in place of an A in the new sequence
        elif nt == 'C': rc.append('G') # adds a G in place of a C in the new sequence
        elif nt == 'G': rc.append('C') # adds a C in place of a G in the new sequence
        elif nt == 'T': rc.append('A') # adds an A in place of a T in the new sequence
        else:           rc.append('N') # adds an N whenever there is a non-ACGT character
    return ''.join(rc) # constructs the new sequence as a string

def translate(dna):
    aas = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if   codon == 'ATG': aas.append('M') # start codon (AUG)
        elif codon == 'TAA': aas.append('*') # stop codon (UAA)
        elif codon == 'TAG': aas.append('*') # stop codon (UAG)
        elif codon == 'TGA': aas.append('*') # stop codon (UGA)
        else:                aas.append('X') # something else
    return ''.join(aas) # constructs the new sequence as a string

def gc_comp(seq):
    return (seq.count('C') + seq.count('G')) / len(seq) # counts the percentage of Gs and Cs in the sequence
    
def gc_skew(seq):
    c = seq.count('C') # counts the number of Cs in the sequence
    g = seq.count('G') # counts the number of Gs in the sequence
    if c + g == 0: return 0 # returns zero if there are no Gs or Cs
    return (g - c) / (g + c) # returns the "skew" towards G or C in the sequence (+ = more G, - = more C)