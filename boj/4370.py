while True:
    try:
        n=int(input())
    except EOFError:
        exit()
    num=1
    while True:
        num*=9
        if num>=n:
            print("Baekjoon wins.")
            break
        num*=2
        if num>=n:
            print("Donghyuk wins.")
            break

# 다른사람 풀이 1
for T in map(int,open(0)):
    n=9;t=0
    while n<T:n*=[2,9][t];t^=1
    print(['Baekjoon','Donghyuk'][t],'wins.')
    
    
# 다른사람 풀이 2
inputList = []

while True:
    try : inputList.append(int(input()))
    except : break
    
inputNum = len(inputList)
def BcanWin(p,n,memo):
    if p >= n:
        return False
    for i in range(2,10):
        if (p*i,n) in memo:
            A = memo[(p*i,n)]
        else:
            A = BcanWin(p*i,n,memo)
            memo[(p*i,n)] = A
        if not A:
            return True
    return False

for i in range(inputNum):
    memo = dict()
    if BcanWin(1,inputList[i],memo):
        print("Baekjoon wins.")
    else:
        print("Donghyuk wins.")
