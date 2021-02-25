#https://www.acmicpc.net/problem/2628

x, y = map(int, input().split())    #[10, 8]  가로 세로
paper = [[0 for j in range(x)] for i in range(y)] #종이 2차원배열
# print(paper)
cut_time = int(input()) # 자르는 횟수 3
pos = list()
for cut in range(cut_time): # 자르는 위치 받기
    pos.append(list(map(int, input().split())))

col = [0,x]
row = [0,y]
for i in pos:
    if i[0] == 1:
        col.append(i[1]) #col = [0,10,4]
    else:
        row.append(i[1]) #row = [0,8,3,2]
col = sorted(col)
row = sorted(row)
# print(col,row)
col_chai=list() # col마다의 너비    [4,6]
row_chai=list() # row마다의 너비    [2,1,5]
for i in range(len(col)-1,0,-1):
    col_chai.append(col[i]-col[i-1])
for i in range(len(row)-1,0,-1):
    row_chai.append(row[i]-row[i-1])
# print(col_chai,row_chai)
print(max(col_chai)*max(row_chai))  #큰거끼리 곱하기 6*5



#처음에는 색종이처럼 인덱스값넣고 셀려고함 -근데 빡센데 그렇게하면
# for i in range(0,len(cut),2):
#     if pos[i] ==1:
#         for X in range(0,pos[i+1]):
#             for Y in range(y):
#                 paper[X][Y] = i
#         for X in range(pos[i+1]:):
#             for Y in range(y):
#                 paper[X][Y] = i+1

#     else:
#         for Y in range(0,pos[i+1]):
#             for X in range(x):
#                 paper[X][Y] = i
#         for Y in range(pos[i+1]:):
#             for X in range(x):
#                 paper[X][Y] = i+1




