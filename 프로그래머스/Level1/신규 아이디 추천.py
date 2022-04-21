# https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    new_id = list(new_id.lower())
    tmp=[]
    for i in range(len(new_id)):
        if new_id[i] in [".","_","-"]:
            tmp.append(new_id[i])
        elif new_id[i].isalpha():
            tmp.append(new_id[i])
        elif new_id[i].isdigit():
            tmp.append(new_id[i])
        else:
            continue

    count=0
    ttmp=[]
    for i in range(len(tmp)):
        if tmp[i] == ".":
            count+=1
            if count>1:
                continue
            else:
                ttmp.append(tmp[i])
        else:
            ttmp.append(tmp[i])  
            count = 0

    if len(ttmp):
        if ttmp[0]==".":
            ttmp = ttmp[1:]
    if len(ttmp):
        if ttmp[-1]==".":
            ttmp = ttmp[:-1]
    if len(ttmp)==0:
        ttmp.append('a')
    if len(ttmp)>=16:
        ttmp = ttmp[:15]
        if ttmp[-1]=='.':
            ttmp = ttmp[:-1]
    if len(ttmp)<=2:
        while(len(ttmp)<3):
            ttmp.append(ttmp[-1])
    ans = ''.join(ttmp)
    return ans