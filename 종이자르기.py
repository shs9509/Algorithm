#https://www.acmicpc.net/problem/2628

x, y = map(int, input().split())
paper = [[0 for j in range(x)] for i in range(y)] 
print(paper)
cut_time = int(input())
pos = list()
for cut in range(cut_time):
    pos.append(map(int, input().split()))


