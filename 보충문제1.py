def graph(a):
    S =list()
    S.append(a)
    visit[a] == True
    while S:
        for w in store[a]:
            if w == 99:
                return 1
            if not visit[w]:
                S.append(a)
                a = w
                visit[w] = True
                break
        else:
            a = S.pop()
    return 0 
    

for j in range(10):
    tc_num, num = list(map(int, input().split()))
    save = list(map(int, input().split()))
    store = [[] for _ in range(100)]
    visit = [False for _ in range(101)]
    for i in range(0, num):
        a, b = save[2*i-2], save[2*i-1]
        store[a].append(b)
    print('#{} {}'.format(tc_num, graph(0)))
