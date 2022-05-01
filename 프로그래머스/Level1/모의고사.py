# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    on=0
    tw=0
    th=0
    for i in range(len(answers)):
        if answers[i] == one[(i%5)]:
            on+=1
        if answers[i] == two[(i%8)]:
            tw+=1
        if answers[i] == three[(i%10)]:
            th+=1
    tmp = [on,tw,th] # 애를 미리 만들어주고 tmp[1] 이렇게 카운트하면됨
    answer=[]
    if on == max(tmp):
        answer.append(1)
    if tw == max(tmp):
        answer.append(2)
    if th == max(tmp):
        answer.append(3)
    answer.sort()
    return answer