# https://www.acmicpc.net/problem/14620

def flower(pan,seed,s):
    if seed ==3:
        value=0
        for (x,y) in s:
            value +=pan[x][y]
        result.append(value)
        return
    else:
        for x in range(1,scale-1):
            for y in range(1,scale-1):
                for i in range(5):
                    X = x+dr[i]
                    Y = y+dc[i]
                    if (X,Y) in s:
                        break
                else:
                    s.append((x,y))
                    s.append((x+1,y))
                    s.append((x-1,y))
                    s.append((x,y+1))
                    s.append((x,y-1))
                    seed +=1
                    flower(pan,seed,s)
                    seed -=1
                    s.pop()
                    s.pop()
                    s.pop()
                    s.pop()
                    s.pop()

dr=[0,0,0,1,-1]
dc=[0,1,-1,0,0]
scale = int(input())
li = list()
for i in range(scale):
    li.append(list(map(int,input().split())))
s = list()
result = list()
flower(li,0,s)
print(result)
print(min(result))






