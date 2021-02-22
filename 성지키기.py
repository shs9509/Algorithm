#https://www.acmicpc.net/problem/1236
a = input().split()     # 행, 열을 받아서 split 로 나눈다.  ### '4  4' ->['4','4']

row=int(a[0])   # 행    ### 4
column=int(a[1])    # 열    ### 4
rectangular= list() # 경비원 배치 리스트

count_row = 0       #가로로 봤을 때 필요한 경비원 수  
count_column = column   #세로로 봤을 때 필요한 경비원 수

for i in range(row):
    rectangular.append(input()) # 경비원배치를 받는다.  ###['....', '...X', 'X...', '....']
#print(rectangular)

for i in range(row):        # 가로열끼리 살펴본다.  ###['(....)', '(...X)', '(X...)', '(....)']
    if 'X' not in rectangular[i]:   # 해당 가로열에 경비원이 없으면
        count_row += 1      # 경비원이 필요하다.

for i in range(column):     # 세로열끼리 살펴본다. ###['(.)...', '(.)..X', '(X)...', '(.)...']
    for j in range(row):    
        if rectangular[j][i]=='X': # 경비원있으면
            count_column -= 1   # 경비원이 필요없다.
            break       # 반복문 아웃!

#### 근데 애는 왜 뺴냐? 세로열이라 하나의 스트링으로 묶여있지 않아서 not in 을 못썻다! ####

if(count_row>count_column): #가로 세로에서 더큰값이 필요한 경비원 수!
    print(count_row)
else:
    print(count_column)
            

#  l = input()
# position=[[0]*i]*j
# for a in range(i):
#     for b in range(j):
#         position[i][j].insert(input())

# print(position)