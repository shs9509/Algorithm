#0715 두 용액 : https://www.acmicpc.net/problem/2470

# n = int(input())
# li = list(map(int, input().split()))
# li = sorted(li)
# # print(li)
# end = n-1
# start = 0
# best_start =0
# best_end =0
# zin=4000000000
# while start<end: 
#     mix = li[start]+li[end] # 이게 문제 였음
#     if abs(zin) >= abs(li[start]+li[end]):
#         zin = li[start]+li[end]
#         best_start = start
#         best_end = end
#         if zin ==0:
#             break
#     if mix <= 0: # 여기도 zin 이였음
#         start +=1
#     else:
#         end -=1
# print(li[best_start],li[best_end])

N = int(input())
li = list(map(int,input().split()))
li.sort()
start = 0
end = N-1
i_want_zero = 100000000000
ans = []
before = li[start]+li[end]


while(start<end):
    sum_val = li[start]+li[end]
    tmp = abs(li[start]+li[end])
    if tmp < i_want_zero:
        ans =[]
        i_want_zero = tmp
        ans.append(li[start])
        ans.append(li[end])
    if sum_val>0:
        end-=1
    elif sum_val<0:
        start+=1
    else:
        break
    
print(ans[0],ans[1])