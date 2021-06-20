import re

N=int(input())
rand_serial=[]
serial=[[] for _ in range(51)]
for i in range(N):
    tmp=input()
    rand_serial.append(tmp)

#print(rand_serial)

for i in range(N):
    serial[len(rand_serial[i])].append(rand_serial[i])

#print(serial)

for i in range(51):
    if len(serial[i])==0:
        continue

    for j in range(len(serial[i])):
        numbers=re.findall("\d", serial[i][j])
        
        numbers=list(map(int,numbers))
        serial[i][j]=[sum(numbers),serial[i][j]]
    serial[i].sort()

    for j in range(len(serial[i])):
        print(serial[i][j][1])
    
