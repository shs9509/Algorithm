#https://www.acmicpc.net/problem/1059
# n= input()
# n=int(n)
# m=list(map(int,input().split()))
# m.sort()
# o=input()
# o=int(o)
# count=0
# count_li=list()

# if n==1:
#     count += m[0]-2
# for i in range(n-1):
#     if o>m[i] and o<m[i+1]:
#         for j in range(o-m[i]):
#             count += m[i+1]-o
#         count_li.append(count)
#         count=0
# if(len(count_li)!=0):
#     a = max(count_li)
#     a -= 1
#     print(a)
# else:
#     print(count)

import sys
input=sys.stdin.readline

l=int(input())
a=list(map(int,input().split()))
a=[0]+a
a.sort()
n=int(input())

left=0
right=0
if n in a:
    print(0)
    sys.exit()

for x in a:
    if n>x:
        left=x+1
    else:
        right=x-1
        break
print(left,right)
print(right-left+(right-n)*(n-left))


