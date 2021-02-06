import sys

a=sys.stdin.readline()
b,c=a.split()
b=int(b)
c=int(c)
k=list()
answer=list()


for i in range(b):
    d=input()
    k.append(d)

# print(k)

for p in range(b-7):
    for j in range(c-7):
        m=0
        n=0
        for z in range(p,8+p):
            for x in range(j,8+j):
                if (z+x)%2:
                    if k[z][x]=='B':
                        m += 1
                    else:
                        n += 1
                else:
                    if k[z][x]=='W':
                        m += 1
                    else:
                        n += 1
        answer.append(m)
        answer.append(n)
# print(answer)
l=min(answer)
print(l)

