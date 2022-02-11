# https://www.acmicpc.net/problem/18513

# pond, house = map(int,input().split())
# pond_pos = list(map(int,input().split()))
# pond_pos.sort()
# # print(pond_pos)

# distance = 1
# dfs_li = list()
# visited = set()
# for i in pond_pos:
#     visited.add(i)
#     dfs_li.append((i,1))
# count=0
# buildIn=0
# while(dfs_li):
#     pos = dfs_li.pop(0)
#     for i in [1,-1]:
#         if (pos[0]+i) in visited:
#             continue
#         else:
#             visited.add(pos[0]+i)
#             count+= pos[1]
#             dfs_li.append((pos[0]+i,pos[1]+1))
#             buildIn+=1
#         if buildIn == house:
#             dfs_li=list()
#             break

# print(count)
# # print(in_house)


from collections import deque
n,k = map(int,input().split(" "))
f = list(map(int,input().split(" ")))
q = deque()
visited = dict()
for i in f:
    visited[i] = 0
    q.append(i)

while q:
    if k <= 0:
        break
    x = q.popleft()
    for dx in [x-1,x+1]:
        if dx not in visited and k >0:
            visited[dx] = visited[x]+1
            k -=1
            q.append(dx)

ans = 0
for value in visited.values():
    ans += value
print(ans)