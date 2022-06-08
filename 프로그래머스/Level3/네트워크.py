# def solution(n, computers):
#     answer = 0
#     conected_check = [False for _ in range(n)]
#     network_count = 0 
#     def dfs(start):
#         nonlocal conected_check
#         conected_check[start] = True
#         tmp = [start]
#         while(tmp):
#             start = tmp.pop()
#             for i in range(n):
#                 if conected_check[i] == False:
#                     if computers[start][i]==1:
#                         conected_check[i] = True
#                         tmp.append(i)
#                     else:
#                         continue
#                 else:
#                      continue   
            
    
#     for i in range(n):
#         if conected_check[i] == False:
#             dfs(i)
#             answer+=1
#     return answer


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer