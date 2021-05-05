#https://www.acmicpc.net/problem/14501

def maximum_earning(day,earning):
    for j in range(day,date+1):
        if j+li[j][0]-1<date+1:
            earn.append(earning+li[j][1])
            maximum_earning(j+li[j][0],earning+li[j][1])          

date = int(input())
li = list()
li.append(0)
earn = list()
earn.append(0)
for i in range(date):
    li.append(list(map(int,input().split())))

maximum_earning(1,0)
print(max(earn))


# 91%에서 멈추는데 그것은 0일때를 고려안해서
