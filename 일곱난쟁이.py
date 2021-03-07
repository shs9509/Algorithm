#https://www.acmicpc.net/problem/2309
heigth = list()
for i in range(9):
    heigth.append(int(input())) # 9명의 난쟁이 키리스트
# print(heigth)

visit = [False] * 9
order = []
li = list()
flag = True
def perm(n,m,val):
    global flag
    if flag == False: # 합이 100인것을 찾으면 즉시 함수를 나올수있게한다.
        return  
    if n == 7:
        if sum(order) == val:   #합이 100이라면 그 원소값을 정렬하고 print
            order.sort()
            for i in order:
                print(i) 
            flag = False  
        # return 1
    for k in range(m):
        if visit[k]:
            continue
        else:
            visit[k] = True
            order.append(heigth[k])
            perm(n+1,m,val)
            # if perm(n+1,m,val) == 1:
            #     return 1
            visit[k] = False
            order.pop()

perm(0,9,100)

