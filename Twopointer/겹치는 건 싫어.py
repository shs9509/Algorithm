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

# from sys import stdin
# from collections import deque

# n, k = map(int, input().split())
# arr = list(map(int, stdin.readline().split()))

# def answer():
#   global n, k, arr
#   startIndex, maxCount = (0, 0)
#   cnt = [0]*100001
#   for i in range(len(arr)):
#     num = arr[i]
#     cnt[num] = cnt[num] + 1
#     if cnt[num] > k:
#       maxCount = max(maxCount, i-startIndex)
#       while(cnt[num] > k):
#         cnt[arr[startIndex]] = cnt[arr[startIndex]] - 1
#         startIndex += 1
#     else:
#       maxCount = max(maxCount, i-startIndex+1)
#   return maxCount
  
# print(answer())

# 16 3
# 1 2 3 4 5 6 7 8 9 1 1 11 1 2 2 2 =>14
full_length, at_least = map(int,input().split())
li = list(map(int,input().split()))
# 객체로 만들자
obj={}
max_length = 0
count=0
start = 0
for i in range(full_length): #3 2 5 5 6 4 4 5(7) 7
  value = li[i]
  # 값이 객체에 있음
  if value in obj:
    obj[value] +=1
    if obj[value] > at_least: #추가했는데 최소값을 넘김
      if max_length<count:
        max_length = count
      for j in range(start,i+1): #앞에 있는거를 땡김
        count -=1
        start = j+1 #시작점 계속 바꿔줌
        m_value = li[j]
        obj[m_value] -=1
        if m_value == value:
          break
      count +=1
    else:
      count +=1 # 길이 1 추가     
  # 값이 객체에 없음 
  else:
    obj[value]=1
    count +=1 # 길이 1 추가


print(max_length)