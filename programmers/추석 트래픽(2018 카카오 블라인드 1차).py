def solution(lines):
    answer = 0
    info=[]
    for time in lines:
        tmp=time.split()[1].split(':')
        fin=float(tmp[0])*3600 + float(tmp[1])*60 + float(tmp[2])
        start= round(fin - float(time.split()[2][:-1]) + 0.001, 3)
        info.append([start, fin])
    
    for time in info:
        cnt=0
        for dtime in info:
            if time==dtime:
                cnt+=1
                continue
            if 0<dtime[0]-time[1]<1 or dtime[0]<time[1]<=dtime[1]:
                cnt+=1
        if cnt>answer:
            answer=cnt
    return answer
