import re
import sys

fin=sys.argv[1]
fout=sys.argv[2]
print(fin)
print(fout)

fr = open(fin, "r")
fw = open(fout, "w")

lines = fr.readlines()

all = dict()

for line in lines:
    linelist=line.split()
    txt=linelist[2]
    if txt != '443':
        item = linelist[0] + " " + linelist[5]
        if item in all:
            all[item] = all.get(item) + 1
        else:
            all.update({item: 1})

for k, v in all.items():
    fw.write(k + "\n")
    fw.write(str(v) + "\n")
