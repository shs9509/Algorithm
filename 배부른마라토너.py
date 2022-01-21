#https://www.acmicpc.net/problem/10546

# maratoner = int(input())
# li = list()
# li_a = list()
# for i in range(maratoner):
#     li.append(input())

# for j in range(maratoner-1):
#     li_a.append(input())
# # for i in li:
# #     if li.count(i)%2==1:
# #         print(i)
# #         break
# #     else:
# #         continue

# while True:
#     if li[0] in li_a:
#         li.pop(0)
#     else:
#         b = li.pop(0)
#         break
# print(''.join(li))

import sys
input = sys.stdin.readline

N = int(input())
# person : 참가한 사람들의 dict
# finish : 완주한 사람들의 dict
person = dict()
finish = dict()
answer = ""
for _ in range(N) :
    name = input().rstrip()
    if name in person :
        person[name] += 1
    else :
        person[name] = 1

for _ in range(N-1) :
    name = input().rstrip()
    if name in finish :
        finish[name] += 1
    else :
        finish[name] = 1


for n in person.keys() :
    #  참가자에는 있지만 완주자에는 없다면 해당 키가 정답
    if n not in finish :
        answer = n
        break
    else :
        #  참가자의 value와 완주자의 value가 다르다면 해당 키가 정답
        if person[n] != finish[n] :
            answer = n
            break
print(answer)