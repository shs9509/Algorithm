def mov(li,mov):    # 움직임에 따른 함수
    
    if mov =='R':
        li[0] +=1
    if mov =='L':
        li[0] -=1
    if mov =='B':
        li[1] -=1
    if mov =='T':
        li[1] +=1
    if mov =='RT':
        li[0] +=1
        li[1] +=1
    if mov =='LT':
        li[0] -=1
        li[1] +=1
    if mov =='RB':
        li[0] +=1
        li[1] -=1
    if mov =='LB':
        li[0] -=1
        li[1] -=1
    
    return li

def cancel_mov(li,mov): # 움직임 취소에 따른 함수
    if mov =='R':
        li[0] -=1
    if mov =='L':
        li[0] +=1
    if mov =='B':
        li[1] +=1
    if mov =='T':
        li[1] -=1
    if mov =='RT':
        li[0] -=1
        li[1] -=1
    if mov =='LT':
        li[0] +=1
        li[1] -=1
    if mov =='RB':
        li[0] -=1
        li[1] +=1
    if mov =='LB':
        li[0] +=1
        li[1] +=1
    return li

king_ps=list()  # 킹의 자리(숫자) A1 -> 11
stone_ps=list() # 돌의 자리(숫자) A2 -> 12
king, stone, times = list(input().split())  # A1, A2, 움직임횟수
times=int(times)
col = ['A','B','C','D','E','F','G','H'] # A1 은 11 로 바꿔주기 위한 리스트

for i in range(len(col)):
    if king[0] == col[i]:
        king_ps.append(i+1)  # A -> 1
        king_ps.append(int(king[1]))
    if stone[0] == col[i]:
        stone_ps.append(i+1) # A -> 1
        stone_ps.append(int(stone[1]))
while times !=0:
    moving = input()    # RT면 
    mov(king_ps,moving) # RT에 따라 11 -> 22
    
    if king_ps == stone_ps: # 킹과 돌이 겹칠경우
        mov(stone_ps,moving)    # 돌이 움직인다.
        if (0 in stone_ps) or ( 9 in stone_ps): # 근데 돌이 밖에 나간다면
            cancel_mov(king_ps,moving)  # 돌과 킹의 움직임 취소!
            cancel_mov(stone_ps,moving)
    if (0 in king_ps) or ( 9 in king_ps):   #킹이 밖으로 나간다면
        cancel_mov(king_ps,moving)  # 킹 움직임 취소!
    times -=1

answer_k=list() # 킹의 최종 위치
answer_s=list() # 돌의 최종 위치
a = king_ps[0]
answer_k.append(col[a-1])   #  11 -> A1
answer_k.append(str(king_ps[1]))
b = stone_ps[0]
answer_s.append(col[b-1])   #  12 -> A2
answer_s.append(str(stone_ps[1]))

print(''.join(answer_k))
print(''.join(answer_s))