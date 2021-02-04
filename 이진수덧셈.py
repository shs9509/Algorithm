#문제 https://www.acmicpc.net/problem/1252
import sys

a=sys.stdin.readline()
b=a.split()
c=int(b[0],2)+int(b[1],2)  # 10진수 int(sd,10) 10생략! 
print(c,format(c,'b'))

# d='0b'+b[0]
# e='0b'+b[1]
