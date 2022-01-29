# https://www.acmicpc.net/problem/14467

li = ['?' for _ in range(11)]
see_times = int(input())
move_count = 0 
for i in range(see_times):
    N, Pos = map(int,input().split())
    if li[N] == '?':
        li[N]=Pos
    elif li[N] != Pos:
        move_count +=1
        li[N] = Pos

print(move_count)