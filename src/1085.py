x,y,w,h=map(int,input().split())

distance=w-x
if h-y<distance:
    distance=h-y
if x<distance:
    distance=x
if y<distance:
    distance=y

print(distance)
