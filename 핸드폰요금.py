# 문제 https://www.acmicpc.net/problem/1267

Y=0
M=0
sec_list=''
t= list()
numbers=input()
sec_list=(input())
# print(sec_list.split())
# print(sec_list)
t =sec_list.split()
# print(sec_list,t,sec_list.split())
# t.sort()
# print(t)

# sec_list=list()
# numbers=input()
# sec_list=(input())
# sec_list.split()
# print(sec_list)

for sec in t:
    Y += (int(sec)//30)*10 + (10 if int(sec)%29 else 0)
    M += (int(sec)//60)*15 + (15 if int(sec)%59 else 0)

if Y> M:
    print(f'M {M}')

elif Y==M:
    print(f'Y M {Y}')

else:
    print(f'Y {Y}')


# d왜틀린거야 빡치네
# 야발!