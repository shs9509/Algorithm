from collections import deque

def solution(n, edge):
    check = [-1 for _ in range(n+1)]
    linked_list=[[] for _ in range(n+1)]
    for e in edge:
        a, b = e
        linked_list[a].append(b)
        linked_list[b].append(a)

    tmp = deque([1])
    check[1] = 1
    while(tmp):
        start = tmp.popleft()
        for i in linked_list[start]:
            if check[i]== -1:
                tmp.append(i)
                check[i] = check[start]+1
    if max(check)>0:
        return check.count(max(check))
    else:
        return 0



def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer