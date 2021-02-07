import sys

a=sys.stdin.readline()
y,x=a.split()
y=int(y)
x=int(x)
k=list()
answer=list()


for i in range(y):
    d=input()
    k.append(d)

# print(k)

for Y in range(y-7):
    for X in range(x-7):
        count_one=0
        count_two=0
        for check_y in range(Y,8+Y):
            for check_x in range(X,8+X):
                if (check_y+check_x)%2:
                    if k[check_y][check_x]=='B':
                        count_one += 1
                    else:
                        count_two += 1
                else:
                    if k[check_y][check_x]=='W':
                        count_one += 1
                    else:
                        count_two += 1
        answer.append(count_one)
        answer.append(count_two)
# print(answer)
l=min(answer)
print(l)

