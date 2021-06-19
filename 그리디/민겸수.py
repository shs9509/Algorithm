#0620 민겸수 :  https://www.acmicpc.net/problem/21314


# 가장작은거 K = 5, 그리고 연속된 M
# 가장 큰거 M뒤에 무조건 K연결 그외엔 K=5

def max_val(W):
    global max_answer
    for i in W:
        if i == 'M':
            s.append(i)
        else:
            s.append(i)
            if s:
                max_answer+='5'
                s.pop()
                while s:
                    s.pop()
                    max_answer+='0'
    if s:
        max_answer+='1'
        s.pop()
        while s:
            s.pop()
            max_answer+='1'
    return

def min_val(W):
    global min_answer
    if W[0]=='M':
        min_answer+='1'
    else:
        min_answer+='5'
    for i in range(1,len(W)):
        if W[i]=='M':
            if W[i-1]=='M':
                min_answer+='0'
            else:
                min_answer+='1'
        else:
            min_answer+='5'
    return

word = list(input())
s= list()
c= list()
max_answer=''
min_answer=''
min_val(word)
max_val(word)
print(max_answer)
print(min_answer)

        