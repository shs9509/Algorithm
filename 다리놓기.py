import sys

def river_bridge(a,b):
    count =0
    if a !=1:
        for i in range(1,b-a+1):
            count += river_bridge(a,b-i)
        count += river_bridge(a-1,b-1)
    else:
        count += b
    return count

n= int(sys.stdin.readline())
for i in range(n):
    a=sys.stdin.readline()
    c=a.split()
    print(river_bridge(int(c[0]),int(c[1])))


# def factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num


# T = int(input())

# for _ in range(T):
#     n, m = map(int, input().split())
#     bridge = factorial(m) // (factorial(n) * factorial(m - n))
#     print(bridge)

# mCn (m-n)!n!