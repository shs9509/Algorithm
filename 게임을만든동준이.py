#https://www.acmicpc.net/problem/2847

level_num = int(input())    # 레벨 갯수
score_list = list()         # 레벨마다 얻는 점수

for i in range(level_num):
    score_list.append(int(input()))

gap = 0 #조정한 점수 값

for j in range(len(score_list)-1,0,-1): # 점수를 뒤에서 부터 순회한다.
    									#(j가 올라갈수로 수가 작아진다.)
    if score_list[j]>score_list[j-1]:   # 정상
        continue
    else:
        gap += score_list[j-1] - score_list[j] + 1   #조정하는 값은 계속 쌓는다.
        score_list[j-1] = score_list[j]-1   # 큰자리의 1을 빼서 값을 정해줌
        
        # 8 -> 10 이면
        # 8 -> 7 로 만들어줘야한다.
        # 3은 gap에 추가 , 10은 7로 만든다.

print(gap)       

# 자칫하면 난이도가 엄청 올라간다.
# 1~ 10레벨인데 중간에 5의 자리가 3레벨 이라면? 
#  + - 해서 정렬시키는 문제였다면?