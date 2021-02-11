def move(li,mov):
    
    if mov =='R':
        li[0] +=1
    if mov =='L':
        li[0] -=1
    if mov =='B':
        li[1] -=1
    if mov =='T':
        li[0] +=1
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

def cancel_move(li,mov):
    if mov =='R':
        li[0] -=1
    if mov =='L':
        li[0] +=1
    if mov =='B':
        li[1] +=1
    if mov =='T':
        li[0] -=1
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
        li[0] -=1
        li[1] -=1
    return li

king_ps=list()
stone_ps=list()
king, stone, times = list(input().split())
col = ['A','B','C','D','E','F','G','H']

for i in range(len(col)):
    if king[0] == col[i]:
        king_ps.append(i+1)
        king_ps.append(int(king[1]))
    if stone[0] == col[i]:
        stone_ps.append(i+1)
        stone_ps.append(int(stone[1]))

for j in times:
    move = input()
    print(king_ps)
    move(king_ps,move)
    
    if king_ps == stone_ps:
        move(stone_ps,move)
        if '9' in stone_ps:
            cancel_move(king_ps,move)
    if '9' in king_ps:
        cancel_move(king_ps,move)

print(king_ps, stone_ps)
