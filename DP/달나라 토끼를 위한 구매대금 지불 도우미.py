#https://www.acmicpc.net/problem/17212

val = int(input())
li =[0]+[999999 for _ in range(val)]
j = len(li)

if j>7:
    li[1] = 1
    li[2] = 1
    li[5] = 1
    li[7] = 1
elif 7>=j>5:
    li[1] = 1
    li[2] = 1
    li[5] = 1
elif 5>=j>2:
    li[1] = 1
    li[2] = 1
elif 2>=j>1:
    li[1] = 1


for i in range(1,val+1):
    if i>7:
        li[i] = min(li[i-1]+1,li[i-2]+1,li[i-5]+1,li[i-7]+1,li[i])
    elif 7>=i>5:
        li[i] = min(li[i-1]+1,li[i-2]+1,li[i-5]+1,li[i])
    elif 5>=i>2:
        li[i] = min(li[i-1]+1,li[i-2]+1,li[i])
    elif 2>=i>1:
        li[i] = min(li[i-1]+1,li[i])

print(li[val])