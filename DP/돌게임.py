#https://www.acmicpc.net/problem/9655
n=int(input())
li= [0,1,0,1]

for i in range(4,n+1):
    if li[i-1]==0 and li[i-3]==0:
        li.append(1)
    elif li[i-1]==1 and li[i-3]==1:
        li.append(0)
if li[n]==1:
    print('SK')
else:
    print('CY')