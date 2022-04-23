# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num = {"ze":['0',2], "on":['1',1],"tw":['2',1],"th":['3',3],"fo":['4',2],"fi":['5',2],"si":['6',1],"se":['7',3],"ei":['8',3],"ni":['9',2]}
    problem = list(s)
    i = 0
    result =""
    string =""
    while i<len(problem):
        if problem[i].isdigit():
            result+=problem[i]
            i+=1
        else:
            if len(string)==2:
                result+=num[string][0]
                i +=num[string][1]
                string =""
            else:
                string +=problem[i]
                i+=1
    
    return int(result)