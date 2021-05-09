<<<<<<< HEAD
# tc = int(input())
# num = int(input())
# li =list()
# for i in range(num):
#     li.append(list(map(int,input().split())))
# sum_val =0
# for i in li:
#     sum_val += sum(i)

# choice = num/2
# choice_li=[n for n in range(choice)]

# print(choice_li,li)


def taste(A):
    total = 0
    for i in A:
        for j in A:
            if i != j:
                total += arr[i][j]
    return total
 

def select(a): # a번째 자리 결정
    global min_dif
    c = [1, 0]
    if sum(check) == N//2: # 6개중 3개가 결정되면[000111] check에 1인 원소가 3개있는 경우
        A = []
        B = []

        for k in range(len(check)):
            if check[k]:# 체크가 1인 원소들
                A.append(k)
            else:   # 체크가 0인 원소들
                B.append(k)
        A_result = taste(A)
        B_result = taste(B)
        # 결과값 비교
        if abs(A_result - B_result) < min_dif:
            min_dif = abs(A_result - B_result)
    # 종료
    elif a == N:
        return
    else:
        # 조합을 만들기 위한 반복, 재귀
        for i in range(2):
            check[a] = c[i] # a원소에 1넣고 넘기기 or 0 넣고넘기기
            if check[0]: # 1XXXXX, 0XXXXX 두가지로 나눠짐[1100] [1010] [1001] // [0011]
                select(a+1) # 한쪽의 경우만 생각하면 되기떄문
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N [1001]
    min_dif = 987654321
    select(0)
    print('#{} {}'.format(t, min_dif))