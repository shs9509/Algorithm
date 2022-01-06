#https://www.acmicpc.net/problem/7568

num = int(input())
li= list()
for i in range(num):
    li.append(list(map(int,input().split())))

# print(li)

rank_li =[1]*num
for i in range(1,num):
    for j in range(i-1,-1,-1):
        # print(i,j)
        if li[i][0] < li[j][0]:
            if li[i][1] < li[j][1]:
                rank_li[i]+=1
        elif li[i][0] > li[j][0]:
            if li[i][1] > li[j][1]:
                rank_li[j]+=1

print(' '.join(map(str,rank_li)))
