I = [l.strip() for l in open('numbers.txt')]

L = []
for elf in ('\n'.join(I)).split('\n\n'):
    l = 0
    for x in elf.split('\n'):
        l += int(x)
    L.append(l)
L = sorted(L)

#First Part
print(L[-1])
#Second Part
print(L[-1]+L[-2]+L[-3])