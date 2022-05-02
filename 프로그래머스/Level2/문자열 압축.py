# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer=[len(s)]
    tmp = list()
    for i in range(1,len(s)//2+1):
        for j in range(0,len(s),i):
            tmp.append(s[j:j+i])
        count = 1
        ttmp=[]
        for k in range(0,len(tmp)-1):
            if k==(len(tmp)-2): #끝에 도달
                if tmp[k]==tmp[k+1]:
                    ttmp.append(str(count+1))
                    ttmp.append(tmp[k])
                    break
                else:
                    if count >1:
                        ttmp.append(str(count))
                    ttmp.append(tmp[k])
                    ttmp.append(tmp[-1])
                    break
            else:
                if tmp[k]==tmp[k+1]:
                    count+=1
                else:
                    if count >1:
                            ttmp.append(str(count))
                    ttmp.append(tmp[k])
                    count = 1
        ttmp=''.join(ttmp)
        answer.append(len(ttmp))
        tmp= []
    return min(answer)