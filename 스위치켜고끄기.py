#https://www.acmicpc.net/problem/1244

switch_num = int(input())   #8개
switch = list(map(int, input().split())) #[0,1,0,1,0,0,0,1]
stu_num = int(input())  # 2명
stu_li =list() #[[1,3], [2,3]]
for i in range(stu_num):
   stu_li.append(list(map(int, input().split())))
 
for stu in stu_li:
    if stu[0] == 1: # 남자의 경우
        number =stu[1]    # 받은 숫자
        i=1             # ?배수
        pos_number = number # 스위치의 위치
        while True:
            pos_number = i*number   # 스위치의 위치는 받은위치의 배수
            if pos_number > len(switch):  # 배수가 스위치를 넘어가면 break
                break
            else:
                switch[pos_number-1] = int(not switch[pos_number-1]) # 배수의 스위치를 스위치한다. 
            i += 1  
    else:   # 여자의 경우
        number =stu[1]    # 받은 숫자
        i=1 # 양쪽의 거리
        position = number -1 # 실질적인 위치(배열에서)
        switch[position] = int(not switch[position])    # 일단 받은 숫자의 스위치 스위치
        while len(switch)>position+i and position-i>-1: # 스위치의 범위를 넘지않는 동안
            if switch[position+i] == switch[position-i]:# 양쪽이 같은 경우
                switch[position+i] = int(not switch[position+i]) # 앞쪽 변경
                switch[position-i] = int(not switch[position-i]) # 뒤쪽 변경
            else: break
            i += 1

j=0
while j<len(switch):

    print(switch[j],end=' ')    # 20개넘어가면 다른줄로 넘어감
    j += 1
    if not j %20:
        print('')

'''    
 막 어렵지는 않았는데 1부터 시작해서 헷갈렸다.
 그리고 20개 넘어가면 줄바뀌는 것도 좀 귀찮(?)았다.
'''