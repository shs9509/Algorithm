a, b = list(map(int, input().split())) # 요구 알파벳수, 주어진 알파벳수
words = list(map(ord, input().split()))
words.sort()
#최소 1개의모음 최소2개의 자음 
# 3개를 일단 고르면 나머지로 바꾸기
# mo = list()
# za = list()
# for i in words:
#     if i in ['i','e','a','o','u']:
#         mo.append(i)
#     else:
#         za.append(i)

## 모음한개 꺼내고 자음두개 꺼내고 나머지리스트 합쳐서 n-3 개 꺼내고 
# 애네들 합쳐서 n개의 원소를 가진 리스트를 순열을 만든다.

## 아니면 일단 n개 꺼내고 순열로 만들고 자음 모음 개수판별 = 이게 구현은 더쉬울듯?
order = []
visit = [False]*b


def perm(start,n,k):
    if n == k:
        count_mo =0
        count_za =0
        for k in order:
            if chr(k) in ['i','e','a','o','u']:
                count_mo +=1
            else:
                count_za +=1
        if count_mo>=1 and count_za>=2:
            for m in order:
                print(chr(m),end='')
            print('')
        return
    for i in range(start,b):
        if visit[i] == True:
                continue
        else:
            visit[i] = True
            order.append(words[i])
            perm(i+1,n+1,k)

            visit[i] = False
            order.pop()

perm(0,0,a)