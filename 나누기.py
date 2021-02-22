#https://www.acmicpc.net/problem/1075
import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
a=(a//100)*100
while True:
    if a%b:
        a += 1
    else:
        c= (a%100 if a%100>9 else '0'+str(a%100))
        print(c)
        break
    
