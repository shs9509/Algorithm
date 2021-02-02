dict_num = {'1':2 ,'2':3,'0':4,'3':3,'4':3,'5':3,'6':3,'7':3,'8':3,'9':3}
answer = list()

while True:
    number= input()
    if 0 in number:
        break
    a=1
    for i in number:
        a+=dict_num[i]
        a+=1
    answer.append(a)
    
for i in answer:
    print(i)