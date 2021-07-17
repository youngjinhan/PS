score=[0 for _ in range(5)]
for i in range(5):
    score[i]=int(input())
    if score[i]<40:
        score[i]=40
print(sum(score)//5)
