def solution(citations):
    answer = leng=len(citations)
    cnt1=0
    cnt2=0
    while answer>=0:
        for i in range(leng):       
            if citations[i]>=answer:
                cnt1+=1
            elif citations[i]<=answer:
                cnt2+=1
        if answer<=cnt1 and answer>=cnt2:
            break
        answer-=1
        cnt1=0
        cnt2=0
    return answer
