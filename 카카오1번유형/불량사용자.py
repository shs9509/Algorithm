#0627 불량사용자 https://programmers.co.kr/learn/courses/30/lessons/64064


def ban_f(on,s,p,l,B):
    if p == l:
        on.append(sorted(s))
        return
    else:
        for b in B[p]:
            if b in s:
                continue
            else:
                s.append(b)
                ban_f(on,s,p+1,l,B)
                s.pop()

def solution(user_id, banned_id):     
    ban_list= [[]for _ in range(len(banned_id))]
    length = len(banned_id)
    for j in range(length):
        for user in range(len(user_id)):
            if len(user_id[user])==len(banned_id[j]):
                for i in range(len(banned_id[j])):
                    if banned_id[j][i]== '*' or banned_id[j][i]==user_id[user][i]:
                        continue
                    else:
                        break
                else:
                    ban_list[j].append(user)
            else:
                continue
            
    S = list()
    L = list()
    new_L = list()
    ban_f(L,S,0,length,ban_list)
    # print(L)
    for i in range(len(L)):
        if L[i] in new_L:
            continue
        else:
            new_L.append(L[i])
    # print(new_L)
    return len(new_L)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])

###################################
def solution(user_id, banned_id):     
    ban_list= [[]for _ in range(len(banned_id))]
    length = len(banned_id)
    for j in range(length):
        for user in range(len(user_id)):
            if len(user_id[user])==len(banned_id[j]):
                for i in range(len(banned_id[j])):
                    if banned_id[j][i]== '*' or banned_id[j][i]==user_id[user][i]:
                        continue
                    else:
                        break
                else:
                    ban_list[j].append(user)
            else:
                continue
            
    S = list()
    L = list()
    new_L = list()
    
    def ban_f(on,s,p,l,B):
        if p == l:
            on.append(sorted(s))
            return
        else:
            for b in B[p]:
                if b in s:
                    continue
                else:
                    s.append(b)
                    ban_f(on,s,p+1,l,B)
                    s.pop()
    
    ban_f(L,S,0,length,ban_list)
    # print(L)
    for i in range(len(L)):
        if L[i] in new_L:
            continue
        else:
            new_L.append(L[i])
    # print(new_L)
    return len(new_L)

#####################################################
################  nonlocal 이용  ####################
#####################################################

#  solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])

def solution(user_id, banned_id):     
    ban_list= [[]for _ in range(len(banned_id))]
    length = len(banned_id)
    for j in range(length):
        for user in range(len(user_id)):
            if len(user_id[user])==len(banned_id[j]):
                for i in range(len(banned_id[j])):
                    if banned_id[j][i]== '*' or banned_id[j][i]==user_id[user][i]:
                        continue
                    else:
                        break
                else:
                    ban_list[j].append(user)
            else:
                continue
    print(ban_list)
    S = list()
    L = list()
    new_L = list()
    
    def ban_f(p):
        nonlocal L
        nonlocal S
        nonlocal length
        nonlocal ban_list
        
        if p == length:
            L.append(sorted(S))
            return
        else:
            for b in ban_list[p]:
                if b in S:
                    continue
                else:
                    S.append(b)
                    ban_f(p+1)
                    S.pop()
    ban_f(0)
    
    print(L)
    for i in range(len(L)):
        if L[i] in new_L:
            continue
        else:
            new_L.append(L[i])
    print(new_L)
    return len(new_L)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])
# 스트링으로 만들고 셋해버리기
# 딕셔너리 키로 판별 