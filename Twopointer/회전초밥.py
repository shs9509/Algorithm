# https://www.acmicpc.net/problem/15961

plate_num,sushi,continue_eat,coupon = map(int,input().split())
li= list()
for i in range(plate_num):
    li.append(int(input()))

# print(li)
li +=li
dict_sushi = {}
max_sushi = 0
for i in range(0,continue_eat):
    if li[i] in dict_sushi:
        dict_sushi[li[i]]+=1
    else:
        dict_sushi[li[i]]=1
# print(dict_sushi)

for j in range(continue_eat,len(li)):
    if li[j] in dict_sushi:
        dict_sushi[li[j]]+=1
    else:
        dict_sushi[li[j]]=1

    if li[j-continue_eat] in dict_sushi:
        if dict_sushi[li[j-continue_eat]]==1:
           dict_sushi.pop(li[j-continue_eat])
        else:
            dict_sushi[li[j-continue_eat]]-=1

    if coupon in dict_sushi:
        length = len(dict_sushi)
    else:
        length = len(dict_sushi)+1
    
    max_sushi = max(length,max_sushi)

print(max_sushi)