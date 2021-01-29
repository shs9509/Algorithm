answer = list()     # 답을 넣을 리스트
num=list()      # 연산할 숫자를 넣는 리스트

for i in range(3):      # 케이스가 3개이므로 3번 돌린다.
    count=input()
    for i in range(int(count)):
        num.append(int(input()))    # input를 처음엔 count, 그다음 count 만큼 값을 받는다.
    if sum(num)>0:      # sum을 통해서 리스트의 부호판별
        answer.append('+')
    elif sum(num)==0:
        answer.append('0')
    else:
        answer.append('-')    
    num.clear()     # 한번 연산을 끝내고 다음 리스트의 연산을 위해 clear한다.             

for i in range(3):
    print(answer[i])        #지금까지 연산한 값을 출력   