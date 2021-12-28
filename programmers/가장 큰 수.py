def solution(numbers):
    
    new_num=list(map(str,numbers))
    answer=sorted(new_num,key=lambda x: 3*x, reverse=True)
    return str(int(''.join(answer)))
    
    
# 잘못된 답 : 반례 - [45,454]
#     new_num=[]
#     maxLeng=0
#     for num in numbers:
#         string=str(num)
#         new_num.append([string,len(string)])
#         if len(string)>maxLeng:
#             maxLeng=len(string)
#     for num in new_num:
#         if num[1]<maxLeng:
#             div,mod=divmod(maxLeng,num[1])
#             num[0]=num[0]*div+num[0][:mod]
    
#     new_num.sort(reverse=True)
#     return str(int(''.join(list(map(lambda x: ''.join(x[0][:x[1]]),new_num)))))
