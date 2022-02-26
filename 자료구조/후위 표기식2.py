# https://www.acmicpc.net/problem/1935
N = int(input())
li = list(input())
num =list()
for i in range(N):
    num.append(input())
check_dict={}
count =0
for i in li:
    if i in ['*','-','/','+']:
        continue
    else:
        if i in check_dict:
            continue
        else:
            check_dict[i]=int(num[count])
            count+=1
# print(check_dict)

tmp =[]
for i in li:
    if i == '*':
        tmp.append(tmp.pop(-2) * tmp.pop())
    elif i == '+':
        tmp.append(tmp.pop(-2) + tmp.pop())
    elif i == '-':
        tmp.append(tmp.pop(-2) - tmp.pop())
    elif i == '/':
        tmp.append(tmp.pop(-2) / tmp.pop())
    else:
        tmp.append(check_dict[i])
print("{:.2f}".format(tmp[0]))