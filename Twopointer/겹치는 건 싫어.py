#0627 겹치는 건 싫어 : https://www.acmicpc.net/problem/20922

length, n = map(int, input().split())
li = list(map(int,input().split()))
save = [0 for _ in range(length+1)]
save_li= list()

count = 0
for i in range(length):
    # print(save)
    save[li[i]] +=1
    count +=1
    if save[li[i]]>n:
        save = [ 0 for _ in range(length+1)]
        save[li[i]] +=1
        save_li.append(count-1)
        count = 0
save_li.append(count)
# print(save_li)
print(max(save_li))
