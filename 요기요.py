#('John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; 
# John Evan Doe; Jane Doe; Peter Brian Parker', 'Example')

def solution(S, C):
    # write your code in Python 3.6
    C = C.lower()
    S = ' '+S
    result = list()
    full_name = S.split(';')

    for i in full_name:
        result.append(i[1:])
        i= i.lower()
        name = i.replace('-',' ').split(' ')
        name.pop(0)
    
        if len(name)==4:
            name[2] = name[2]+name.pop()
            name[2] = name[2][:8]
        elif len(name)==3:
            name[2] = name[2][:8]
        else:
            name[1] = name[1][:8]
    
        if len(name)==2:
            count =2
            email = '<'+name[0]+'.'+name[1]+'@'+C+'.'+'com'+'>'+';'
            while str(email) in result:
                    email = '<'+name[0]+'.'+name[1]+str(count)+'@'+C+'.'+'com'+'>'+';'
                    count+=1
            result.append(email)    
                   
        else:
            count =2
            email = '<'+name[0]+'.'+name[2]+'@'+C+'.'+'com'+'>'+';'
            while str(email) in result:
                    email = '<'+name[0]+'.'+name[2]+str(count)+'@'+C+'.'+'com'+'>'+';'
                    count+=1
            result.append(email) 
    return ' '.join(result)[:-1]




