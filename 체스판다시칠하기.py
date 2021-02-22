#https://www.acmicpc.net/problem/1018
import sys

a=sys.stdin.readline()
y,x=a.split()
y=int(y)
x=int(x)
chess_board=list()
answer=list()


for i in range(y):
    color=input()
    chess_board.append(color)   #체스판 입력받는다.

# print(chess_board)

for Y in range(y-7):    # 세로로 8칸에서 추가된 만큼 순회
    for X in range(x-7):    # 가로로 8칸에서 추가된 만큼 순회
        count_one=0     # BW패턴과 차이나면 개수 +1
        count_two=0     # WB패턴과 차이나면 개수 +1
        for check_y in range(Y,8+Y):    # 8칸 세로 순회 
            for check_x in range(X,8+X):    # 8칸 가로 순회
                if (check_y+check_x)%2:     # BW의 위치를 파악하면 x,y좌표의 합이 홀짝으로 패턴을 가진다.
                    if chess_board[check_y][check_x]=='B':
                        count_one += 1
                    else:
                        count_two += 1  
                else:
                    if chess_board[check_y][check_x]=='W':
                        count_one += 1
                    else:
                        count_two += 1      # BW WB 패턴을 한꺼번에 판별을 진행한다.
        answer.append(count_one)
        answer.append(count_two)
# print(answer)
l=min(answer)   # 가장적은 차이를 보인것을 출력
print(l)

