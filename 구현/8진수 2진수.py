#https://www.acmicpc.net/problem/1212

li = list(input())
if len(li)==1 and li[0]=='0':
    print('0')
else:
    result= list()
    for i in li:
        s = int(i)//4
        k = int(i)%4
        result.append(str(s))
        s = k//2
        k = k%2
        result.append(str(s))
        s = k//1
        result.append(str(s))

    while True:
        if result[0]=='0':
            result.pop(0)
        else:
            break
    print(''.join(result))

#############################
print(format(int(input(),8),'b'))