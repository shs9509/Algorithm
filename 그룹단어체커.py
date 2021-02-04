import sys
a= sys.stdin.readline()
count =0
for i in range(int(a)):
    b=sys.stdin.readline()
    while True:
        for i in range(len(b)):
            if b[i]==b[i+1]:
                b.pop(i+1)
                break
        for i in b:
            if b.count(i)>1:
                break
        else:
            count +=1     
print(count)
        