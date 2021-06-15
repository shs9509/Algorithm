#https://www.acmicpc.net/problem/2839

n= int(input())

li=[-1,-1,-1,1,-1,1]

for i in range(6, n+1):
    if li[i-3] !=-1 and li[i-5] !=-1:
        li.append(min(li[i-3]+1,li[i-5]+1))
    elif li[i-3] !=-1 and li[i-5] ==-1:
        li.append(li[i-3]+1)
    elif li[i-3] ==-1 and li[i-5] !=-1:
        li.append(li[i-5]+1)
    else:
        li.append(-1)

print(li[n])

##
#3을 빼면서 5로 나눌수있으면 되는거
