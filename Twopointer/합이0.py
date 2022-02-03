# https://www.acmicpc.net/problem/3151
# [-4, 2, 2, 2]
# [-5, 0, 5, 5, 5]
N = int(input())
li = list(map(int,input().split()))
li.sort()
# print(li)
count=0
for j in range(N-2):
    s= j+1
    e= N-1
    prev_e=N-1
    while(s<e):
        tmp = li[s]+li[e]
        if tmp+li[j]==0:
            # print(s,e,j,li[s],li[e],li[j])
            if li[s]==li[e]:
                count += e-s
            else:
                if prev_e>e:
                    prev_e = e
                    while prev_e>=0 and (li[prev_e]==li[e]):
                        prev_e-=1
                count+=e-prev_e+1
            s+=1
        elif tmp+li[j]<0:
            s+=1
        else:
            e-=1
print(count)


