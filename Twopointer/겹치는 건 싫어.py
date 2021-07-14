#0627 겹치는 건 싫어 : https://www.acmicpc.net/problem/20922

# length, n = map(int, input().split())
# li = list(map(int,input().split()))
# save = [0 for _ in range(length+1)]
# save_li= list()

# count = 0
# for i in range(length):
#     # print(save)
#     save[li[i]] +=1
#     count +=1
#     if save[li[i]]>n:
#         save = [ 0 for _ in range(length+1)]
#         save[li[i]] +=1
#         save_li.append(count-1)
#         count = 0
# save_li.append(count)
# # print(save_li)
# print(max(save_li))

###################################

from sys import stdin
from collections import deque

n, k = map(int, input().split())
arr = list(map(int, stdin.readline().split()))

def answer():
  global n, k, arr
  startIndex, maxCount = (0, 0)
  cnt = [0]*100001
  for i in range(len(arr)):
    num = arr[i]
    cnt[num] = cnt[num] + 1
    if cnt[num] > k:
      maxCount = max(maxCount, i-startIndex)
      while(cnt[num] > k):
        cnt[arr[startIndex]] = cnt[arr[startIndex]] - 1
        startIndex += 1
    else:
      maxCount = max(maxCount, i-startIndex+1)
  return maxCount
  
print(answer())