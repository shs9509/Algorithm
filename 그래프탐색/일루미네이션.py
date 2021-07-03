#0704 일루미네이션 https://www.acmicpc.net/problem/5547

from itertools import dropwhile


width, height = map(int,input().split())
li =list()
li.append([0 for i in range(width+2)])
for h in range(height):
    li.append([0]+list(map(int, input().split()))+[0])
li.append([0 for i in range(width+2)])

# print(li)

dr_hol = [-1,0,0,-1,1,1]
dc_hol = [1,1,-1,0,1,0]
dr_zzak = [0,0,-1,-1,1,1] 
dc_zzak = [-1,1,0,-1,-1,0]

visit = [[False for _ in range(width+2)]for _ in range(height+2)]

count = 0
s =list()
s.append((0,0))

def light(v, S):
    global count
    while S:
        a,b = S.pop()
        for j in range(6):
            if a%2:
                A = a+dr_hol[j]
                B = b+dc_hol[j]
            else:
                A = a+dr_zzak[j]
                B = b+dc_zzak[j]
            if 0<=A<height+2 and 0<=B<width+2:
                if v[A][B]==False and li[A][B]==0:
                    v[A][B]= True
                    S.append((A,B))
                elif li[A][B]==1:
                    count+=1
    return count

print(light(visit,s))


