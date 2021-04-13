#https://www.acmicpc.net/problem/2479

def dfs(s,e,visited):
    visited = visited+[s]
    for j in range(1,num+1):
        if j not in visited: # 방문 안했던 비교할 코드
            count_code = 0
            for code in range(length): # 코드확인
                if li[s][code] != li[j][code]:
                    count_code += 1
                    if count_code>1:
                        break
            if count_code == 1: # 해밍코드가 확인되면
                if j == e:  # 도착코드일경우
                    visited = visited+[j]
                    answer.append(visited)
                    return
                else:   # 그저 해밍코드일경우 
                    dfs(j, e, visited) # j를 시작으로 탐색
    else:            
        return

num, length = map(int, input().split())
# print(num, length)
answer = list()
li= [[0]]
for i in range(1,num+1):
    li.append(list(input()))
# print(li)
visit=[]
start, end = map(int, input().split())

dfs(start,end,visit)

if len(answer)==0: # answer에 아무것도 없다면 답이없다!
    print(-1)
else:
    small_len = num+1 # 최소경로를 찾는 과정 (길이가 가장 짧은것!)
    for an in range(len(answer)): 
        if len(answer[an])<=small_len:
            small_len = an
    print(' '.join(map(str,answer[an])))

    



'''
코드들을 다 순회를 돌아서 해밍코드인지 확인
확인한후 해당 해밍코드에 방문체크를 한다.
그러면 방문체크리스트가 필요하겟네

1에서 3,5를 갈수있고 3에서 4 > 2로 도착하는데
5 같은 가망이 없는애를 어떻게 없애지??
'''