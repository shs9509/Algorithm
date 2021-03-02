#https://www.acmicpc.net/problem/15650
n, m = map(int, input().split())  # 3 1 # 123 에서 부분집합 길이 1

arr = [1 + i for i in range(n)]   # 숫자 리스트     [1,2,3]
used = [False] * n                # 중복숫자 체크   [false false false]
order = []                                # 출력할 수열
 

def perm(start,k):
    if k == m:
        print(*order)
        return

    for i in range(start,n):
        if used[i]: continue

        used[i] = True
        order.append(arr[i])

        perm(i+1,k + 1)

        used[i] = False
        order.pop()


perm(0,0)
