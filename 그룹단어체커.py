#https://www.acmicpc.net/problem/1316
import sys
a= input()
count =0
ali=list()
for i in range(int(a)):
    b=input()
    print(b)
    for j in range(len(b)-2):
        if b[j]!=b[j+1]:
            ali.append(b[j])
    if b[len(b)-2]!=b[-1]:
        ali.append(b[-1])
    for k in ali:
        if ali.count(k)>1:
            break
        else:
            continue
    else:
        count +=1
    print(count,ali)
print(count)
        