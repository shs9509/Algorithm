#https://www.acmicpc.net/problem/19532

a,b,c,d,e,f = map(int, input().split())

x= (c*e-b*f)/(a*e-d*b)
y= (c*d-a*f)/(b*d-a*e)
print(int(x),int(y))