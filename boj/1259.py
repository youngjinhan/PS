digit=''
while True:
    digit=input()
    if digit=='0':
        break
    if digit==digit[::-1]:
        print("yes")
    else:
        print("no")
