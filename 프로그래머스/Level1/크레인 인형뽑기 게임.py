# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    tmp = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]==0:
                continue
            else:
                tmp.append(board[i][m-1])
                board[i][m-1]=0
                break
    count=0
    while(True):
        ttmp=[]
        if(len(tmp)<=1):
            break
        for j in range(0, len(tmp)-1):
            if tmp[j]==tmp[j+1]:
                count+=2
                ttmp+=tmp[j+2:]
                break
            else:
                ttmp.append(tmp[j])
        else:
            ttmp.append(tmp[-1])
        if tmp == ttmp:
            break
        else:
            tmp = ttmp
    return count