# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    tmp = []
    name = {}
    for i in record:
        small = list(i.split())
        tmp.append(small)
    for i in tmp:
        if len(i)==3:
            name[i[1]] = i[2]
    for i in tmp:
        say =""
        if i[0]=="Enter":
            say += name[i[1]]+"님이 들어왔습니다."
            answer.append(say)
        elif i[0]=="Leave":
            say += name[i[1]]+"님이 나갔습니다."
            answer.append(say)
            
        
    
    return answer