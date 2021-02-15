import sys

def river_bridge(a,b): # (3,6) 시작
    count=0
    if a==1:
        count += b  
        #(1,4) 나 (1,3) 의 경우 4가지 3가지의 경우를 가지므로 b가 경우의수값
    else:
        for i in range(1,b-a+2):
            count +=river_bridge(a-1,b-i) # (2,5) (2,4) (2,3) (2,2) 호출
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
#     return num  #조합을 구현하기 위한 팩토리얼 함수 구현 


# T = int(input())

# for _ in range(T):
#     n, m = map(int, input().split())
#     bridge = factorial(m) // (factorial(n) * factorial(m - n)) #mCn
#     print(bridge)

# # mCn (m-n)!n!