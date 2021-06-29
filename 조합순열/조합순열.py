# [1,2,3,4,5]
# [6,7,8,9,10]

# 순서있는 순열 
# arr = "ABCD"
# order = []      # 순열 저장
# cnt = 1
# def perm(k, n, used):
#     if k == n:
#         global cnt
#         print("%2d> %s" % (cnt, " ".join(order)))
#         cnt += 1
#         return
#     for i in range(n):
#         if used & (1 << i): continue
#         order.append(arr[i])
#         perm(k + 1, n, used | (1 << i))
#         order.pop()
# perm(0, 4, 0)

# 중복있는 순열
# arr = [1,2,3,4,5]

# def per(pos,s):
#     if pos == 5:
#         print(s)
#         return
#     else:
#         for i in range(5):
#             s.append(arr[i])
#             per(pos+1,s)
#             s.pop()
# per(0,[])

# 중복있는 순열
arr = [1,2,3,4,5]

def per(pos,s):
    if pos == 5:
        print(s)
        return
    else:
        for i in range(5):
            if arr[i] in s:
                continue
            else:
                s.append(arr[i])
                per(pos+1,s)
                s.pop()
per(0,[])