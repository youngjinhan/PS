train=[list(map(int,input().split())) for _ in range(10)]

sum_num=max_num=0
for i in train:
    sum_num+=i[1]-i[0]
    if sum_num>max_num:
        max_num=sum_num

print(max_num)
