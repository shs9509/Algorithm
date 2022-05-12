# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    stages.sort()
    people_num = len(stages)
    fail =[0 for _ in range(N+1)]
    for i in range(1, N+1):
        time = stages.count(i)
        if people_num==0:
            fail[i]=0
            continue
        fail[i] = time/people_num
        people_num-=time
    answer = []
    for i in range(1, len(fail)):
        if answer:
            for j in range(len(answer)):
                if fail[answer[j]]<fail[i]:
                    answer.insert(j,i)
                    break
            else:
                 answer.append(i)   
        else:
            answer.append(i)        
    return answer