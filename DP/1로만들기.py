# #https://www.acmicpc.net/problem/1463
# n = int(input())

# dp = [0 for _ in range(n+1)]

# for i in range(2, n+1):
#     dp[i] = dp[i-1] + 1  

#     if i%2 == 0 and dp[i] > dp[i//2] + 1 :
#         dp[i] = dp[i//2]+1
        
#     if i%3 == 0 and dp[i] > dp[i//3] + 1 :
#         dp[i] = dp[i//3] + 1
        
# print(dp[n])

#########################
n = int(input())
li = [0,0,1,1]

for i in range(4,n+1):
    li.append(li[-1]+1)

    if i%2==0:
        li[-1]= min(li[i//2]+1,li[-1])

    if i%3==0:
        li[-1]= min(li[i//3]+1,li[-1])
print(li)