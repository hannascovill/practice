import re

fh= input("Enter File Name")
if len(fh) < 1: fh = 'regex_sum_226301.txt'
Handle = open(fh)
output = []
for line in Handle:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    if len(y) >0:
        for n in y:
            n = float(n)
            #print(n)
            output.append(n)
#print(output)
#sum = sum(output)
print(sum)
