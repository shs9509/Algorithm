# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    count =0
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)
    for i in set_lost:
        if i-1 in set_reserve:
            set_reserve.remove(i-1)
            count+=1
        elif i+1 in set_reserve:
            set_reserve.remove(i+1)
            count+=1
    answer = n-len(set_lost)+count
    return answer