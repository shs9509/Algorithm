# https://www.acmicpc.net/problem/20436

li = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]

left, right = map(int,input().split())

for x in range(len(li)):
    for y in range(len(li[x])):
        if li[x][y]== left:
            left_x = x
            left_y = y
        if li[x][y] == right:
            right_x = x
            right_y = y
    