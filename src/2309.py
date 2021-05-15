small=list(int(input()) for _ in range(9))

fake_sum=sum(small)-100
#print(fake_sum)

for i in range(9):
    for j in range(9):
        if i>=j or i>=len(small) or j>=len(small):
            continue
        if small[i]+small[j]==fake_sum:
            small.remove(small[j])
            small.remove(small[i])
            fake_sum=0
            break

small.sort()

for i in small:
    print(i)
         
