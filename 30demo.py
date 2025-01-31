import sys

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)


print('hey "dude" don\'t tell me what to do')

nts = ('a','b','c','d')

for i, nt in enumerate(nts):
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])

for nt, name in zip(nts, names):
    print(nt, name)

text = 'good day          to you'
words = text.split()
print(words)

print(s, s[::], s[::1], s[::-1])

print(sys.argv)

print('-'.join(list('ABCDE'))[3:6])