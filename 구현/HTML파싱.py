# https://www.acmicpc.net/problem/22859

# String = input()
# String = String[6:-7] # main
# String_div = String.split("<")
# tmp =[]
# for i in String_div:
#     if "title" in i:
#         tmp.append("title : "+i[11:-2])
#         continue
#     elif "br" in i:
#         tmp.append(i[4:])
#         continue
#     elif "i>" in i:
#         tmp.append(i[2:])
#         continue
#     elif "b>" in i:
#         tmp.append(i[2:])
#         continue
#     elif "/" in i:
#         continue
#     else:
#         tmp.append(i)
# # print(tmp)
# tmp =[v for v in tmp if v]
# # print(tmp)

# for j in range(len(tmp)):
#     if tmp[j]=="> ":
#         continue
#     else:
#         if tmp[j]:
#             if "title" in tmp[j]:
#                 if j ==0:
#                     print(tmp[j])
#                 else:
#                     print("")
#                     print(tmp[j])
#             elif "p>" in tmp[j]:
#                 if "title" in tmp[j-1]:
#                     print(tmp[j][2:],end="")
#                 else:
#                     print("")
#                     print(tmp[j][2:],end="")
#                 continue
#             elif tmp[j][0]==">":
#                 print(tmp[j][1:],end="")
#                 continue
#             else:
#                 print(end=tmp[j])

########################################################################################
string = input()
divs = string.split('<div title="')
for i in range(1, len(divs)):
    div = divs[i]
    p_list = div.split('<p>')
    title = p_list.pop(0)
    title = title[:-2]
    print('title :', title)
    # p태그들
    for ps in p_list:
        sentence = ''
        j = 0
        while j < len(ps):
            # 태그기호는 다 제거 '<' 나오면 '>' 나올 때까지 스킵
            if ps[j] == '<':
                for k in range(j+1, len(ps)):
                    if ps[k] == '>':
                        j = k
                        break
            else:
                sentence += ps[j]
            j += 1
        # 띄어쓰기 한칸씩만 만들어주기
        result = sentence.split()
        result = ' '.join(result)
        print(result)
