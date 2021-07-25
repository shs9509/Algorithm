#0718 배열 돌리기 https://www.acmicpc.net/problem/17276
import copy
tc = int(input())

# dr =[1,0,-1,-1,-1,0,1,1]
# dc =[1,1,1,0,-1,-1,-1,0]
dr = [1,1,0,-1,-1,-1,0,1]
dc = [0,-1,-1,-1,0,1,1,1]

for tc_num in range(tc):
    scale, angle = list(map(int, input().split()))
    li= list()
    for s in range(scale):
        li.append(list(map(int,input().split())))
    after_li =copy.deepcopy(li)
    center = scale // 2 # 중앙
    radius = scale // 2 # 반지름
    angle_time = angle //45
    for r in range(1,radius+1):
        for a in range(8):
            after_li[center+(dr[(a+angle_time)%8]*r)][center+dc[(a+angle_time)%8]*r] = li[center+dr[a]*r][center+dc[a]*r]

    # print(after_li)
    for after in after_li:
        print(" ".join(map(str,after)))