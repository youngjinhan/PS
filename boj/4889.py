import re

i=1
while True:
    line=input()
    if line[0]=='-':
        break
    while True:
        nline=re.sub("{}","",line)
        if nline==line:
            break
        else:
            line=nline
    
    left=line.count('}')
    right=line.count('{')

    print(str(i)+". "+str(round(left/2+0.1)+round(right/2+0.1)))
    i+=1
