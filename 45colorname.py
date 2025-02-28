import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

matchscore = []
colors = []
rgbs = []

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

with open(colorfile, 'rt') as fp:
    for line in fp:
        words = line.split()
        matchscore.append(words)

for line in matchscore:
    colors.append(line[0])
    rgbs.append(line[2].split(','))

for i in range(len(rgbs)):
    rgbs[i].insert(0,colors[i])
    for j in range(1,4):
        rgbs[i][j] = int(rgbs[i][j])

rgb_ds = []

for row in rgbs:
    dist = dtc(row[1:4],[R,G,B])
    rgb_ds.append([row[0],dist])

final_color = None
min = rgb_ds[0][1]

for row in rgb_ds:
    if row[1] < min:
        min = row[1]
        final_color = row[0]

print(final_color)
