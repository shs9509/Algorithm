# https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    count =0
    while(progresses):
        if progresses[0] >=100:
                progresses.pop(0)
                speeds.pop(0)
                count+=1
        else:
            if count:
                answer.append(count)
            for i in range(len(progresses)):
                progresses[i]+=speeds[i]
            count=0
    if count:
        answer.append(count)
    return answer