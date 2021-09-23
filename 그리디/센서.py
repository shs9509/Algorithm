#https://www.acmicpc.net/problem/2212

# 6
# 2
# 1 6 9 3 6 7
# 1 3 6 6 7 9
#  2 3 0 1 2
# 0 1 2 2 3
senser_num = int(input())
center_num = int(input())
senser_pos = list(map(int,input().split()))
senser_pos = sorted(senser_pos)

dis = list()
for i in range(1,senser_num):
    dis.append(senser_pos[i]-senser_pos[i-1])

dis = sorted(dis)
print(sum(dis[0:senser_num-center_num]))