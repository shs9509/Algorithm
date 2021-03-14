#https://www.acmicpc.net/problem/3980

tc = int(input())
for tc_num in range(tc):
    spec = list()
    for num in range(11):
        spec.append(list(map(int,input().split())))

    def perm(k,cursum):
        global ans
        if k == 11:
            if cursum >= ans:
                ans = cursum
        return
            for i in range(11):
                if used[i] or spec[k][i] == 0: continue
                used[i] = 1
                perm(k + 1, cursum + spec[k][i])
                used[i] = 0
    
    used = [0] * 11
    ans = 0
    perm(0, 0)
    print(ans)
