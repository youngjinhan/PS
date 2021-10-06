def solution(answers):
    answer = []
    pick1=[1,2,3,4,5]  # len=5
    pick2=[2,1,2,3,2,4,2,5] # len=8
    pick3=[3,3,1,1,2,2,4,4,5,5] # len=10
    cnt=[0,0,0]
    for i in range(len(answers)):
        if answers[i]==pick1[i%5]:
            cnt[0]+=1
        if answers[i]==pick2[i%8]:
            cnt[1]+=1
        if answers[i]==pick3[i%10]:
            cnt[2]+=1
    for i in range(len(cnt)):
        if cnt[i]==max(cnt):
            answer.append(i+1)
    return answer
