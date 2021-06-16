def zohap(lis,leng,start,sta):
    global count
    if len(sta)> count:
        print(sta)
        count =len(sta)
    for i in range(start,leng):
        if len(sta)==0:
            sta.append(lis[i])
            zohap(lis,leng,i+1,sta)
            sta.pop()
        else:
            if sta[-1]<lis[i]:
                sta.append(lis[i])
                zohap(lis,leng,i+1,sta)
                sta.pop()
            else:
                continue
    return

length = int(input())
li = list(map(int,input().split()))
s = list()
count =1
zohap(li,length,0,s)
print(count)


#########################################
x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)

print(max(dp))

10 20 30 10 40
1  2   3  1  4
