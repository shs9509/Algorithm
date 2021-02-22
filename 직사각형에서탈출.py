#https://www.acmicpc.net/problem/1085
position = input()
position=position.split(' ')
x=int(position[0])
y=int(position[1])
w=int(position[2])
h=int(position[3])

if x>(w-x):     #좌우 거리비교
    x=w-x
if y>(h-y):     #상하 거리비교
    y=h-y

if x>y:
    print(y)
else:
    print(x)
