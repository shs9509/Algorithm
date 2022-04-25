# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for j in range(len(completion)):
        if completion[j]==participant[j]:
            continue
        else:
            return participant[j]
    else:
        return participant[-1]