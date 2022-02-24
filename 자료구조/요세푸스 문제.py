# https://www.acmicpc.net/problem/1158

N,K = map(int,input().split())

tmp = [n for n in range(1,N+1)]
# 1 2 3 4 5 6 7
ans = list()
count =0
pos=-1
# 2
while(tmp):
    count +=1
    pos+=1
    if pos >=len(tmp):
        pos=0
    if count ==K:
        count=0
        ans.append(tmp.pop(pos))
        pos-=1
print("<"+", ".join(map(str,ans))+">")


# N, K = map(int, input().split())
# circle = list(range(1, N+1))
# i = 0
# ans = []
# while circle:
#     i = (i+K-1) % len(circle)
#     ans.append(circle.pop(i))
# print('<' + ', '.join(map(str, ans)) + '>')