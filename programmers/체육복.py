def solution(n, lost, reserve):
    length=len(lost)
    answer=n-length
    cur=0 # lost pointer
    for i in range(length):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i]=0
            answer+=1
            
    lost.sort()
    for i in range(length):
        if lost[i]==0:
            continue
        if len(reserve)==0:
            break
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            lost[i]=0
            answer+=1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            lost[i]=0
            answer+=1
    
    return answer
