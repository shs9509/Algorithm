# https://www.acmicpc.net/problem/1874

n= int(input())
li = [ m for m in range(1,n+1) ]
ans = []
result =[]
while(li or ans):
    k = int(input())
    if k in li:
        while(li):
            ans.append(li.pop(0))
            result.append('+')
            if k in ans:
                ans.pop()
                result.append('-')
                break
    elif k in ans:
        if k == ans.pop():
            result.append('-')
        else:
            result.append('NO')
            break
    else:
        result.append('NO')
        break

if 'NO' in result:
    print('NO')
else:
    for i in result:
        print(i)