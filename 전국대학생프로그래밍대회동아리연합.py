a=input()
a=a.split()
number=int(a[0])    # 참가자수
yeesan=int(a[1])    # 예산
building=int(a[2])  # 호텔의 수
weeks=int(a[3])     # 고를수있는 주
cost=list()         # 1인당 숙박비용
num_list=list()     # 주당 투숙 가능한 최대 인원
can_list=list()     # 인원 수용 가능할 경우 비용
for i in range(building):
    c=input()
    cost.append(c)
    d=input()
    d=d.split()
    num_list.append(d)

for p in range(building):   # 빌딩마다 인원을 수용할수있는 확인
    for k in num_list[p]:
        if int(k) > number:
            can_list.append(number*int(cost[p])) 
            # 투숙 가능하다면 비용을 canlist 에 넣는다.

if(len(can_list)==0):   # 예산을 통해서 투숙가능확인
    print("stay home")
elif(min(can_list)>yeesan):
    print("stay home")
else:
    print(min(can_list))





