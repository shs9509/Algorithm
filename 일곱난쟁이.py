#https://www.acmicpc.net/problem/2309
heigth = list()
for i in range(9):
    heigth.append(int(input())) # 9명의 난쟁이 키리스트

visit = [False] * 9
order = []
li = list()
# flag = True
def perm(n,m,val):
    if n == 7:
        if sum(order) == val:   #합이 100이라면 그 원소값을 정렬하고 print
            li.append(order)
            return 1
        return
    for k in range(m):
        if visit[k]:
            continue
        else:
            visit[k] = True
            order.append(heigth[k])
            if perm(n+1,m,val) == 1:
                return 1            #flag외의 방법
            else:
                perm(n+1,m,val)
            visit[k] = False
            order.pop()

perm(0,9,100)
print(li)

