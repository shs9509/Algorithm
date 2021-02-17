def mov(li,mov):
    
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

def cancel_mov(li,mov):
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

king_ps=list()
stone_ps=list()
king, stone, times = list(input().split())
times=int(times)
col = ['A','B','C','D','E','F','G','H']

for i in range(len(col)):
    if king[0] == col[i]:
        king_ps.append(i+1)  # A1  11
        king_ps.append(int(king[1]))
    if stone[0] == col[i]:
        stone_ps.append(i+1)
        stone_ps.append(int(stone[1]))
while times !=0:
    moving = input()
    mov(king_ps,moving) # a1
    
    if king_ps == stone_ps:
        mov(stone_ps,moving)
        if (0 in stone_ps) or ( 9 in stone_ps):
            cancel_mov(king_ps,moving)
            cancel_mov(stone_ps,moving)
    if (0 in king_ps) or ( 9 in king_ps):
        cancel_mov(king_ps,moving)
    times -=1

answer_k=list()
answer_s=list()
a = king_ps[0]
answer_k.append(col[a-1])
answer_k.append(str(king_ps[1]))
b = stone_ps[0]
answer_s.append(col[b-1])
answer_s.append(str(stone_ps[1]))

print(''.join(answer_k))
print(''.join(answer_s))