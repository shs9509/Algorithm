a = input().split()
row=int(a[0])
column=int(a[1])
rectangular= list()
count_row = 0
count_column = column
for i in range(row):
    rectangular.append(input())
# print(rectangular)

for i in range(row):
    if 'X' not in rectangular[i]:
        count_row += 1
for i in range(column):
    for j in range(row):
        if rectangular[j][i]=='X':
            count_column -= 1
            break
if(count_row>count_column):
    print(int(count_row))

else:

    print(int(count_column))  # string 이였어서 안풀림 ㅋㅋㅋㅋ
            

#  l = input()
# position=[[0]*i]*j
# for a in range(i):
#     for b in range(j):
#         position[i][j].insert(input())

# print(position)