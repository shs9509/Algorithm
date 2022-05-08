# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def solution(numbers, target):
    count =0
    def dfs(li,value,pos):
        nonlocal count;
        if pos== len(li):
            if value==target:
                count+=1
        else:
            a = li[pos]
            pos+=1
            dfs(li, value+a,pos)
            dfs(li, value-a,pos)
    dfs(numbers,0,0)
    return count