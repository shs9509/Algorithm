#https://www.acmicpc.net/problem/2851

mush= list()    # 슈퍼마리오가 먹을 버섯
for i in range(10):
    mush.append(int(input()))
sum=0
for j in range(10):
    sum += mush[j] # 일단 버섯값을 더한다.
    if abs(100-sum)<=abs(100-(sum-mush[j])): # 절댓값(abs) 이용해서 100이랑 더가까운것을 고른다.
        continue
    else:
        sum -= mush[j]  # 100에서 더 멀어지면 더햇던 버섯값을 뺀다.
        break

print(sum)