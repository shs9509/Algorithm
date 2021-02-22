#https://www.acmicpc.net/problem/1094
a = input()
a = int(a)

count =0
while a!=0:
    if not a%2:
        a = a/2
    else:
        a = a//2
        count += 1
print(count)        # 이거 그냉 2진수 문제