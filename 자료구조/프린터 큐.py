# https://www.acmicpc.net/problem/1966

# N = int(input())
# result = list()

# for i in range(N):
#     num, important = map(int,input().split())
#     li = list(map(int,input().split()))
#     lis = list()
#     for k in range(num):
#         lis.append((lis[k],k))

#     tmp =list()
#     ans =0
#     for i in range(num):
#         if li[i]<max(li):
#             tmp.append((lis[i]))
#         elif li[i] == max(li):
#             ans +=1
#             a,b = lis.pop(i)
#             if b == important:
#                 print(ans)
#                 break



# for w in result:
#     print(w)

test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split( )))
    imp = list(map(int, input().split( )))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0
    
    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if imp[0]==max(imp):
            order += 1
                        
            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0]=='target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))