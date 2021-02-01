string = input()
string = string.upper()
count_num =list()

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

unique_string = list(set(string))

for char in unique_string:
    count_num.append(string.count(char))
if count_num.count(max(count_num))>1:
    print('?')
else:
    print(unique_string.pop(count_num.index(max(count_num))))
    