#https://www.acmicpc.net/problem/2804
a,b = list(input().split())
a = list(a)
b = list(b)
a_id = 0
b_id = 0
flag =True
for a_idx in range(len(a)): # 가로 
    for b_idx in range(len(b)-1,-1,-1):  #for b_idx in range(len(b)): 이렇게 하면 끝이 된다 ㅇㅅㅇ?
        if (flag == True) and (a[a_idx] == b[b_idx]):
            a_id = a_idx
            b_id = b_idx
            flag =False
    if flag == False:
        break
        
answer =  [['.']*len(a) for _ in range (len(b))]

for i in range(len(a)):
    answer[b_id][i] = a[i]
for j in range(len(b)):    
    answer[j][a_id] = b[j]

for x in answer:
    print(''.join(x))

## 왜막혔는가? 
## 바보같이 배운거 제대로 복습을 안해서
## answer =  [['.']*len(a) for _ in range (len(b))] 중요하다
## 왜 
## a= [','] * n 
## b=a*m              이렇게 했을까
## for b_idx in range(len(b)-1,-1,-1):  #for b_idx in range(len(b)): 이렇게 하면 끝이 된다 ㅇㅅㅇ?
## break를 한꺼번에 벗어나기 위해 flag 를 사용했는데 다른방식이 있을까?
## 