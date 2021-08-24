
# data=[]
# out=[]
# top=0
# result=[]
# n=int(input())

# for _ in range(n):
#     data.append(int(input()))

# for i in data:
#     if i>top:
#         result.append('+'*(i-top))
#     out.append(i)
#     out=list(set(out))
#     top-=1



data=[]
stack=[0]
top=0
out=[]
result=[]
flag=0
n=int(input())
for _ in range(n):
    data.append(int(input()))

cur_input=0
for i in data:
    push_data=stack[top]
    # print(top, stack)
    
    if stack[top]>i:
        flag=1
        print("NO") 
        break
    while cur_input<i:
        cur_input+=1
        stack.append(cur_input)
        top+=1
        result.append("+")
    # print(cur_input, stack)
    if stack[top]>cur_input:
        cur_input=stack[top]
    out.append(stack.pop())
    top-=1
    result.append('-')

if not flag: print('\n'.join(result))
