import copy

def setting(stu,l):
    if len(stu)==0:
        return l
    else:
        student,a,b,c,d = stu.pop(0)
        last_like_count = -1
        s= list()
        for x in range(scale):
            for y in range(scale):
                if l[x][y]==0:
                    s.append((x,y))
                    like_count =0
                    vacant_count =0
                    for i in range(4):
                        X = x+dr[i]
                        Y = y+dc[i]
                        if 0<=X<scale and 0<=Y<scale:
                            if l[X][Y] in [a,b,c,d]:
                                like_count +=1
                            elif l[X][Y]==0:
                                vacant_count +=1
                    if like_count>last_like_count:
                        last_like_count = like_count
                        last_vacant_count = vacant_count
                    elif like_count == last_like_count:
                        if vacant_count > last_vacant_count:
                            last_vacant_count=vacant_count
                        else:
                            s.pop()
                    else:
                        s.pop()
        x,y = s.pop()
        l[x][y] = student
        return setting(stu,l)

            
def score(stu,l):
    last_score=0
    for x in range(scale):
        for y in range(scale):
            count = 0
            for j in stu:
                if j[0]==l[x][y]:
                    for i in range(4):
                        X = x+dr[i]
                        Y = y+dc[i]
                        if 0<=X<scale and 0<=Y<scale:
                            if l[X][Y] in [j[1],j[2],j[3],j[4]]:
                                count +=1
            if count:
                last_score += 10 **(count-1) 
    return last_score

scale = int(input())
student = list() 
dr = [-1,0,1,0]
dc = [0,-1,0,1]

for i in range(scale*scale):
    student.append(list(map(int, input().split()))) # 4 2 5 1 7

student_b = copy.copy(student)
li= [[0 for _ in range(scale)] for _ in range(scale)]

li = setting(student,li)
print(score(student_b,li))