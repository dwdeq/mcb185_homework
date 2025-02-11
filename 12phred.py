import math

def char_to_prob (c):
    q = ord(c) - 33
    p = 10 ** (-q / 10)
    if (p > 0 and p <= 1):  return p
    else:                   return 'None'

def prob_to_char (p):
    if p <= 0:
        return 'None'
    else:
        q = -10 * math.log10(p)
        c = chr(round(q+33))
        return c
    
print(char_to_prob('A'))
print(sep=' ', end='\n')
print(prob_to_char(0.013))