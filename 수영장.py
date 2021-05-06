#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq

def swimming_cost(month,cost):
    if month>=12:
        cost_li.append(cost)
        return
    if schedule[month]*price[0] < price[1]:
        swimming_cost(month+1,cost+schedule[month]*price[0])
    else:
        swimming_cost(month+1, cost+price[1])
    if schedule[month]:
        swimming_cost(month+3,cost+price[2])

tc = int(input())

for tc_num in range(tc):
    price = list(map(int,input().split())) # 1일 1달 3달 1년
    schedule = list(map(int,input().split()))
    cost_li=list() 
    cost_li.append(price[3])  
    swimming_cost(0,0)
    print('#{} {}'.format(tc_num+1,min(cost_li)))






#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq

def swimming_cost(month,cost):
    if month>=12:
        cost_li.append(cost)
        return
    
    if schedule[month]*price[0] < price[1]:
        swimming_cost(month+1,cost+schedule[month]*price[0])
    else:
        swimming_cost(month+1, cost+price[1])
    if schedule[month]:
        swimming_cost(month+3,cost+price[2])

tc = int(input())

for tc_num in range(tc):
    price = list(map(int,input().split())) # 1일 1달 3달 1년
    schedule = list(map(int,input().split()))

    # value = [0]*13
    # count = 0
    # for i in range(1,13):
    #     if schedule[i]:
    #         count +=1 
    #         if schedule[i]*price[0]>= price[1]:
    #             value[i] = value[i-1] + price[1]
    #         else:z
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

    cost_li=list() 
    cost_li.append(price[3])  
    swimming_cost(0,0)
    print('#{} {}'.format(tc_num+1,min(cost_li)))


