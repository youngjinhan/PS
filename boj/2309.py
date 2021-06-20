small=list(int(input()) for _ in range(9))

fake_sum=sum(small)-100

for i in range(9):
    for j in range(9):
        if i>=j or i>=len(small) or j>=len(small):
            continue
        if small[i]+small[j]==fake_sum:
            # 제거할때 small[j]부터 뺴야함. i<j이기 때문에 small[i] 부터 빼면 j가 한칸 앞으로 땡겨지기 때문에 small[j-1]에 값이 저장.
            # small[i]부터 제거하려면 small[j-1]을 제거.
            #small.remove(small[j])
            #small.remove(small[i])
            del small[j]
            del small[i]
            #fake_sum=0   << 필요없음
            break

small.sort()

for i in small:
    print(i)
         
