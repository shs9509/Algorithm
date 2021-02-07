a=input()
a=a.split()
number=int(a[0])
yeesan=int(a[1])
building=int(a[3])
weeks=int(a[4])
cost=list()
week_number=list()
can_list=list()
for i in range(building):
    c=input()
    cost.append(c)
    d=input()
    d=d.split()
    d=list()
    week_number.append(d)

for i,value in enumerate week_number:
    for j in week_number[i]:
        if j>number:
            can_list.append(number*int(cost[i]))

if(len(can_list)==0):
    print("stay home")
else:
    print(min(can_list))





