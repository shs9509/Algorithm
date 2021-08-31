#https://www.acmicpc.net/problem/21317

num = int(input())
li = list()
for i in range(num-1):
    li.append(list(map(int,input().split())))

big = int(input())

##################################################################
# big_jump = int(input())

# lis = list()
# for i in range(num-1):
#     if i==0:
#         lis.append(li[i][0])
#     else:
#         lis.append(li[i-1][0]+li[i][0])

# # print(lis,li)
# for j in range(num-1):
#     if j-2>=0:
#         lis[j] = min(lis[j], lis[j-1]+li[j][0], lis[j-2]+li[j][1] )
    
#     elif j-1>=0:
#         lis[j] = min(lis[j], lis[j-1]+li[j][0])
#     else:
#         continue

#################################################################

lis = list()
def dfs( pos, big_jump, val):
    if pos == num:
        lis.append(val)
        return
    elif pos >num:
        return
    else:
        if big_jump:
            dfs(pos+3, False, val+big)
        dfs(pos+1, big_jump, val+li[pos-1][0])
        dfs(pos+2, big_jump, val+li[pos-1][1])

dfs(1,True,0)
print(min(lis))

#########################################
# DP 로 푸는 방법##########################
#########################################
dp = [[200000, 200000] for _ in range(24)]
dp[0][1] = 0
n = int(input())
energys = []
for _ in range(n - 1):
    s, b = input().split()
    energys.append((int(s), int(b)))
k = int(input())
for i in range(n-1):
    for very_big in range(2):
        dp[i + 1][very_big] = min(dp[i + 1][very_big], dp[i][very_big] + energys[i][0])
        dp[i + 2][very_big] = min(dp[i + 2][very_big], dp[i][very_big] + energys[i][1])
    dp[i + 3][0] = min(dp[i + 3][0], dp[i][1] + k)
print(min(dp[n-1][1], dp[n-1][0]))