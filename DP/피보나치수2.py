#https://www.acmicpc.net/problem/2748
n = int(input())
cnt=0
x=0
y=1
while True:
    if cnt==n:
        break
    cnt +=1
    x,y = y,x+y

print(x)
