# https://www.acmicpc.net/problem/10799

metal = list(input())
# print(metal)
tmp =list()
ans =0
for i in range(len(metal)):
    if  metal[i]=='(':
        tmp.append(metal[i])
    elif metal[i]==')':
        if metal[i-1]=='(':
            tmp.pop()
            ans += len(tmp)
        else:
            tmp.pop()
            ans+=1
print(ans)


