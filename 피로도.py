#https://www.acmicpc.net/problem/22864

A,B,C,M = list(map(int,input().split()))
# print(A,B,C,M)
time = 0
tired = 0
work=0
while(time<24):
    time+=1
    if tired+A>M:
        tired-=C
        if tired<0:
            tired=0
    else:
        tired+=A
        work+=B

print(work)