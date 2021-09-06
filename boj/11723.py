import sys

input=sys.stdin.readline
M = int(input())
result = set()

for _ in range(M):
    args = input().split()
   
    if len(args) == 1:
        if args[0] == "all":
            result = set([i for i in range(1, 21)])
        else:
            result = set()  
    else:
        args[1]=int(args[1])
        if args[0] == "add":
            result.add(args[1])
        elif args[0] == "remove":
            result.discard(args[1])
        elif args[0] == "check":
            print(int(args[1] in result))
        elif args[0] == "toggle":
            if args[1] in result:
                result.discard(args[1])
            else:
                result.add(args[1])
