#https://www.acmicpc.net/problem/2309
heigth = list()
for i in range(9):
    heigth.append(int(input()))
# print(heigth)

visit = [False] * 9
order = []
li = list()
flag = True
def perm(n,m,val):
    global flag
    if flag == False:
        return
    if n == 7:
        if sum(order) == val:
            order.sort()
            for i in order:
                print(i)
            flag = False  
        return
    for k in range(m):
        if visit[k]:
            continue
        else:
            visit[k] = True
            order.append(heigth[k])
            perm(n+1,m,val)
            visit[k] = False
            order.pop()

perm(0,9,100)

