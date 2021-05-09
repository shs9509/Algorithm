#https://www.acmicpc.net/problem/14503

def in_range(x,y):
    if 0<=x<row and 0<=y<col:
        return True
    else:
        return False

def turn_left(direction):
    if direction==0:
        direction=3
    else:
        direction = direction-1
    return direction

def turn_back(direction):
    if direction==0:
        direction=2
    elif direction==2:
        direction=0
    elif direction==3:
        direction=1
    else:
        direction=3
    return direction

def vecum(r,c,d,p):
    global count
    d=turn_left(d)
    if li[r+dr[d]][c+dc[d]] == 0:
        r = r+dr[d]
        c = c+dc[d]
        li[r][c]=3
        count+=1
        vecum(r,c,d,0)        
    else:
        if p == 3:
            d=turn_back(d)
            r=r+dr[d]
            c=c+dc[d]
            if li[r][c] ==1:
                return count
            elif li[r][c] ==3:
                d=turn_back(d)
                return vecum(r,c,d,0)
            else:
                d=turn_back(d)
                count+=1
                return vecum(r,c,d,0)
        else:
            vecum(r,c,d,p+1)
    

row, col = map(int,input().split())
start_r, start_c, start_d = map(int,input().split())
# 0 북쪽, 1 동쪽, 2 남쪽, 3 서쪽

li = list()
for i in range(row):
    li.append(list(map(int,input().split())))

dr=[-1,0,1,0]
dc=[0,1,0,-1]
li[start_r][start_c]=3
count =1
vecum(start_r,start_c,start_d,0)
print(count)
print(li)
