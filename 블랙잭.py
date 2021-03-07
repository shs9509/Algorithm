#https://www.acmicpc.net/problem/2798

num, sum_val = list(map(int , input().split())) # num장의 카드 , sum_val을 넘지 말아야한다.
card = list(map(int , input().split())) # 카드 리스트
visit = [False] * num	# 순열 중복 체크
order =  []	 # 순열이 저장되는 곳
li = list()	 # 카드의 합이 저장되는 곳
def perm(k,n,a):
    if k == 3:	# 3장이니깐
        val = sum(order)	
        if val <= a :
            li.append(val)  # sum_val을 넘지않는 값들을 li에 저장
        return
    for i in range(n):
        if visit[i]:
            continue
        else:
            visit[i] = True
            order.append(card[i])

            perm(k+1, n, a)

            visit[i] = False
            order.pop()

perm(0,num,sum_val)
print(max(li))  # 그안에서 가장 큰값 추출
