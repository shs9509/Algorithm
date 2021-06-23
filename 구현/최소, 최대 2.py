#https://www.acmicpc.net/problem/20053

tc = int(input())
for i in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    print(min(a), max(a))
