a=input()
a=a.split()
number=int(a[0])
yeesan=int(a[1])
building=int(a[2])
weeks=int(a[3])
cost=list()
num_list=list()
can_list=list()
for i in range(building):
    c=input()
    cost.append(c)
    d=input()
    d=d.split()
    num_list.append(d)

for p in range(building):
    for k in num_list[p]:
        # print(k,number)
        if int(k) > number:
            can_list.append(number*int(cost[p]))

# print(can_list)
if(len(can_list)==0):
    print("stay home")
elif(min(can_list)>yeesan):
    print("stay home")
else:
    print(min(can_list))





