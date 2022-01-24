#https://www.acmicpc.net/problem/20546
import copy

money = int(input())
a_money = copy.copy(money)
li = list(map(int,input().split()))

up_count =0
down_count =0
have = 0
for i in range(1,14):
    if li[i]>li[i-1]:
        up_count+=1
        down_count=0
    elif li[i]<li[i-1]:
        down_count+=1
        up_count=0
    else:
        up_count=0
        down_count=0
    if up_count>=3:
        money +=li[i]*have
        have = 0
    if down_count>=3:
        if money==0:
            continue
        got = money//li[i]
        have += got
        money -= got*li[i]
    # print(have,money)

result_a = money+(li[13]*have)

a_have =0
# print(a_money)
for j in range(14):
    a_got = a_money//li[j]
    a_have += a_got
    a_money -= a_got*li[j]
    if a_money ==0:
        break

result_b = a_money+(li[13]*a_have)

# print(result_b,result_a)

if result_a > result_b:
    print('TIMING')
elif result_a < result_b:
    print('BNP')
else:
    print('SAMESAME')