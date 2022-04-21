# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    erase_num =  lottos.count(0)
    match_num = len(set(lottos)&set(win_nums))
    best = 7-erase_num-match_num
    if best > 6:
        best = 6
    worst = 7-match_num
    if worst > 6:
        worst = 6
    
    answer = [best,worst]
    return answer