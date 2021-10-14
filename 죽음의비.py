#https://www.acmicpc.net/problem/22944

import sys
N, M = map(int, sys.stdin.readline().split())
gameList = [int(sys.stdin.readline()) for _ in range(N)]
a = gameList[0]
mylist = []
for _ in range(len(gameList)):
    mylist.append(a)
    b = gameList[a]
    mylist.append(b)
    a = gameList[b]
if mylist[0] == a:
if M in mylist:
    print(mylist.index(M) + 1)
else:
    print('-1')
break
