#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq

'''
이거 풀었던 문제같은데
기억이안남
근데 벽부수기 문제를 응용하면 되지않을까?
'''
tc = int(input())
for tc_num in range(tc):
    scale, K = map(int,input().split())
    li = list()
    for i in range(scale):
        li.append(list(map(int,input().split())))

    start_value = 0
    start_list = list()
    for x in range(scale):
        for y in range(scale):
            if li[x][y]> start_value:
                start_list.clear()
                start_list.append((x,y))
                start_value = li[x][y]
            elif li[x][y] == start_value:
                start_list.append((x,y))
    print(start_list)


