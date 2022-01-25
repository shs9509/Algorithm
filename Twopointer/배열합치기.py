# https://www.acmicpc.net/problem/11728

a_len, b_len = map(int,input().split())
a_li = list(map(int,input().split()))
b_li = list(map(int,input().split()))
c= list(a_li+b_li)
c.sort()
print(' '.join(map(str,c)))