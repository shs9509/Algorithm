#https://www.acmicpc.net/problem/1106



number, cities_num = map(int,input().split())  # (<12, 2)

cities= list()
for i in range(cities_num):
    cities.append(list(map(int, input().split())))

min_li = [0]+[100000000]*(number+101)

for city in cities:
    cost, guest = city # (2,5) (1,1)
    for new_guest in range(guest,number+101):
        min_li[new_guest] = min(min_li[new_guest], min_li[new_guest - guest] + cost)
print(min(min_li[number:number + 101]))