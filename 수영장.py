#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq

tc = int(input())
for tc_num in range(tc):
    price = list(map(int,input().split())) # 1일 1달 3달 1년
    schedule = list(map(int,input().split()))
    schedule.insert(0,0)
    # value = [0]*13
    # count = 0
    # for i in range(1,13):
    #     if schedule[i]:
    #         count +=1 
    #         if schedule[i]*price[0]>= price[1]:
    #             value[i] = value[i-1] + price[1]
    #         else:
    #             value[i] = value[i-1] + schedule[i]*price[0]
    #     else:
    #         count = 0
    #         value[i] = value[i-1]
        
    #     if count >= 3:
    #         if value[i]-value[i-2] >= price[2]:
    #             value[i] = value[i-2] + price[2]
        
    #     if i ==12:
    #         if value[12]>=price[3]:
    #             value[12]==price[3]

    # print(value[12])
    