# https://programmers.co.kr/learn/courses/18/lessons/1882
def solution(strs, t):
    answer = 0
    li = list(t)
    INF = 999999999999
    li_check = [INF for _ in range(len(t))] +[0] #[99,99,99,99,99,99,0]
    for i in range(len(t)-1,-1,-1):# 5 4 3 2 1 0 
        for j in range(i+1,len(t)+1):# 5~6, 4~5
            if j>i+5:
                break
            if t[i:j] in strs:# t[5:6] 있으면
                li_check[i] = min(li_check[i],li_check[j]+1)
    if li_check[0] == INF:
        return -1
    else:
        return li_check[0]