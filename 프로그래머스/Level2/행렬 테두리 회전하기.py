# https://programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    li = [[1 for _ in range(columns) ] for _ in range(rows) ]
    count =1
    for x in range(rows):
        for y in range(columns):
            li[x][y] = count
            count+=1
    
    def rotate(p):
        nonlocal li
        h1, w1, h2, w2 =p
        h1-=1
        w1-=1
        h2-=1
        w2-=1
        w_length = w2-w1+1
        h_length = h2-h1+1
        rotate_li = []
        rotate_li += li[h1][w1:w2+1]
        for i in range(h1+1,h2+1):
            rotate_li.append(li[i][w2])
        tmp = li[h2][w1:w2]
        tmp = tmp[::-1]
        rotate_li+=tmp
        for i in range(h2-1,h1,-1):
            rotate_li.append(li[i][w1])
        # print(rotate_li)
        value = min(rotate_li)

        rotate_li.insert(0,rotate_li.pop())
        # print(rotate_li)
        li[h1][w1:w2+1] = rotate_li[0:w_length]
        rotate_li = rotate_li[w_length:]
        for i in range(h1+1,h2+1):
            li[i][w2] = rotate_li.pop(0)
        tmp = rotate_li[0:w_length-1]
        tmp = tmp[::-1]
        li[h2][w1:w2] = tmp
        rotate_li = rotate_li[w_length-1:]
        for i in range(h2-1,h1,-1):
            li[i][w1] = rotate_li.pop(0)
        # print(li)
        return value
    
    answer =[]
    for i in queries:
        answer.append(rotate(i))
        
    return answer