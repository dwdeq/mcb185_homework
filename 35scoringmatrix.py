import sys
import math

chars = sys.argv[1]
m_score = sys.argv[2]
mm_score = sys.argv[3]

score_mat = []

for row in range(len(chars)+1):
    score_row = []
    for col in range(len(chars)+1):
        if (row == 0 and col == 0):
            score_row.append(' ')
        elif(row == 0):
            score_row.append(chars[col-1:col])
        elif(col == 0):
            score_row.append(chars[row-1:row])
        else:
            if (chars[row-1:row] == chars[col-1:col]):
                s = '+'
                s += m_score
                score_row.append(s)
            else:
                score_row.append(mm_score)
    score_mat.append(score_row)

for row in score_mat:
    for thing in row:
        print(f'{thing: >2}',end = ' ')
    print()