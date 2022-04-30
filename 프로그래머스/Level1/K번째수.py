# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer=[]
    for command in commands:
        start, end, ordr = command
        tmp = array[(start-1):end]
        tmp.sort()
        answer.append(tmp[ordr-1])
    return answer