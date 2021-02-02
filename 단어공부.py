#문제 https://www.acmicpc.net/problem/1157

string = input()    # ///[ Missiissip ]
string = string.upper()     #리스트 값들을 대문자로 통일시켜준다. ///[ MISSIISSIP ]
count_num =list()           #중복 횟수가 들어갈 리스트

unique_string = list(set(string))       #set을 통해서 중복이 사라진 리스트를 만들어준다. ///[M,I,S,P]

for char in unique_string:      #중복이 없는 리스트의 값들을 통해서 
    count_num.append(string.count(char))    #기존 리스트의 중복횟수를 세고 그 값을 리스트에 넣어준다. ///[1,4,4,1]
if count_num.count(max(count_num))>1:       #가장 높은값은 찾아내서 그값이 혼자가 아니면 '?' 출력   ///count(4)==2 > '?'    
    print('?')
else:
    print(unique_string.pop(count_num.index(max(count_num))))   #혼자라면 해당 인덱스를 얻어서 글자를 찾아낸다.
    

# string = input()    # ///[ Missiissip ]
# string = string.upper()     #리스트 값들을 대문자로 통일시켜준다. ///[ MISSIISSIP ]
# count_num =list()           #중복 횟수가 들어갈 리스트
# max_char=''

# second_max=''
# max=0

# for i in string:
#     if string.count(i)>max:
#         max_char = i
#         max_count = string.count(i)
#     if string.count(i)==max_count:
#         if i!=max_char:
#             second_max=i
# if string.count(second_max) == string.count(max_char):
#     print('?')
# else:
#     print(max_char)