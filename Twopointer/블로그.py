#https://www.acmicpc.net/problem/21921

# n, x = map(int, input().split())
# xList = list(map(int, input().split()))

# s = sum(xList[:x])
# l = 0
# r = x - 1
# M = 0
# cnt = 0
# while True:
#     if M < s:
#         cnt = 1
#         M = s
#     elif M == s:
#         cnt += 1
#     r += 1
#     if r == n:
#         break
#     s += xList[r]
#     s -= xList[l]
#     l += 1

# if M == 0:
#     print('SAD')
# else:
#     print(M)
#     print(cnt)

full_length, length = map(int,input().split())
li = list(map(int,input().split()))

# start = sum(li[0:length])
start = sum(li[:length])
max_val = start
count =1
for i in range(length,full_length):
    start = start - li[i-length] + li[i]
    if max_val<start:
        max_val = start
        count=1
    elif max_val == start:
        count+=1
    else:
        continue

if max_val==0:
    print('SAD')
else:
    print(max_val)
    print(count)
