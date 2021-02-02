# 문제 https://www.acmicpc.net/problem/1032

def prompt(file_names):
    short_name_index = 0
    short_name_value = file_names[0]
    long_name_index = 0
    long_name_value = file_names[0]

    for index, value in enumerate(file_names):                         
        if len(value)<len(short_name_value):
            short_name_index = index
            short_name_value = value           # 가장 짧은 단어와 index 추출
    for index, value in enumerate(file_names):
        if len(value)>len(long_name_value):
            long_name_index = index
            long_name_value = value            # 가장 긴 단어와 index 추출

    lenght_gap = len(long_name_value) - len(short_name_value) 

    answer=[0 for i in range(len(short_name_value))]      # [0,0,0,,,0] 짧은 배열 수만큼
    for i in range(lenght_gap):
        answer.append('?')      # 정답 배열을 미리 [0,0,0,,,0????] 상태로 만들어 놓는다.

    for file_name in file_names:
        i=0
        while i<len(short_name_value):      # 가장 짧은 배열을 하나씩 다른 배열들과 비교를 한다.
            if answer[i] !='?':     #'?' 였던 자리가 새로 덮어써지는것을 방지한다.
                if file_name[i] == short_name_value[i]: # 해당 자리의 값이 ? 아니면 비교해서 같으면 짧은배열의 값을 넣어준다.
                    answer[i]=short_name_value[i]
                    i += 1
                else:
                    answer[i]='?'   # 다르다면 그자리에 ? 를 넣어준다.
                    i += 1
            else:
                i +=1                                   
    return ''.join(answer)


number =input()
file_names = list()
for i in range(int(number)):
    file_names.append(input())
print(prompt(file_names))