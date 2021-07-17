#0715 두 용액 : https://www.acmicpc.net/problem/2470



n = int(input())
li = list(map(int, input().split()))
li = sorted(li)
# print(li)
end = n-1
start = 0
best_start =0
best_end =0
zin=4000000000
while start<end: 
    mix = li[start]+li[end] # 이게 문제 였음
    if abs(zin) >= abs(li[start]+li[end]):
        zin = li[start]+li[end]
        best_start = start
        best_end = end
        if zin ==0:
            break
    if mix <= 0: # 여기도 zin 이였음
        start +=1
    else:
        end -=1
print(li[best_start],li[best_end])
    # else:
    #     print(li[past_start],li[past_end])
    #     break

# 5
# -100 -50 20 40 80

# import sys

# n = int(sys.stdin.readline())
# liquid = sorted(list(map(int, sys.stdin.readline().split())))

# pl = 0
# pr = len(liquid) - 1
# limit = liquid[pr] + liquid[0]
# small = 0
# large = 0

# while pl < pr:
#     mix = liquid[pl] + liquid[pr]

#     if abs(mix) <= abs(limit):
#         limit = mix
#         small = pl
#         large = pr
#         if limit == 0:
#             break

#     if mix >= 0:
#         pr -= 1
#     else:
#         pl += 1

# print(liquid[small], liquid[large])