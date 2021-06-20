import math
def solution(progresses, speeds):
    answer = []
    days=[100 for _ in range(len(progresses))]
    for i in range(len(days)):
        days[i]=math.ceil((days[i]-progresses[i])/speeds[i])
    i=0
    count=1
    while i<len(days):
        if count==1:
            std=days[i]
        if i+1<len(days) and std>=days[i+1]:
            count+=1
        else:
            answer.append(count)
            count=1
        i+=1
    print(days)
    return answer
