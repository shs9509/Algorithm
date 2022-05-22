
# https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3
def solution(str1, str2):
    answer = 0
    str1_tmp = list(str1)
    str2_tmp = list(str2)
    li1=[]
    li2=[]
    for i in range(len(str1_tmp)-1):
        word = ''.join(str1_tmp[i:i+2])
        if word.isalpha():
            li1.append(word.upper())
    for i in range(len(str2_tmp)-1):
        word = ''.join(str2_tmp[i:i+2])
        if word.isalpha():
            li2.append(word.upper())
    a = len(li1)
    b = len(li2)
    count = 0
    if a==0 and b==0:
        return 65536
    while(True):
        flag = False
        for i in range(len(li1)):
            for j in range(len(li2)):
                if li1[i]==li2[j]:
                    li1.pop(i)
                    li2.pop(j)
                    count+=1
                    flag = True
                    break
                else:
                    continue
            if flag:
                break
        else:
            break
    return int((count/(a+b-count))*65536)