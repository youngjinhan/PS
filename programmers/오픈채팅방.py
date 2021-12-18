def solution(record):
    answer = []
    info=[]
    idNick={}
    for rec in record:
        args=rec.split(' ')
        if args[0]=='Enter':
            info.append([args[1],'님이 들어왔습니다.'])
            idNick[args[1]]=args[2]
        elif args[0]=='Leave':
            info.append([args[1],'님이 나갔습니다.'])
        else:
            idNick[args[1]]=args[2]
    for inf in info:
        inf[0]=idNick[inf[0]]
        answer.append(''.join(inf))
    return answer
