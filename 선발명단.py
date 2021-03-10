tc = int(input())
spec = list()
for i in range(11):
    spec.append(map(int, input().split()))

# 자바애들은 DFS로 풀었다는데 흠.. 왜지?


visit = [[False for _ in range(11)]for a in range(11)]
order = []

def perm(n,k):
    if k==n:
        return  
    for i in range(11):
        for j in range(11):
            if visit[i][j] == True:
                continue
            else:
                if spec[i][j]>0:
                    visit[i][j] = True
                    order.append(spex[i][i])
                perm(n+1,k)

                visit[i][j] = False
                order.pop()
