#https://www.acmicpc.net/problem/13022
li = list(input())
if li[0] !='w':
    print(0)
elif li[-1]!='f':
    print(0)
else:
    w_count=0
    o_count=0
    l_count=0
    f_count=0
    for i in range(len(li)-1):
        if li[i]=='w':
            w_count +=1
            if li[i+1]=='o':
                continue
            elif li[i+1]=='w':
                continue
            else:
                print(0)
                break
        elif li[i]=='o':
            o_count +=1
            if li[i+1]=='l' and w_count==o_count:
                continue
            elif li[i+1]=='o':
                continue
            else:
                print(0)
                break
        elif li[i]=='l':
            l_count +=1
            if li[i+1]=='f' and w_count==o_count and o_count==l_count:
                if i==len(li)-2:
                    if w_count==o_count and o_count==l_count and l_count== f_count+1:
                        print(1)
                        break
                    else:
                        print(0)
                        break
                else: 
                    continue
            elif li[i+1]=='l':
                continue
            else:
                print(0)
                break
        elif li[i]=='f':
            f_count +=1
            if li[i+1]=='w' and w_count==o_count and o_count==l_count and l_count== f_count:
                continue
            elif li[i+1]=='f':
                if i==len(li)-2:
                    if w_count==o_count and o_count==l_count and l_count== f_count+1:
                        print(1)
                        break
                    else:
                        print(0)
                        break
                else: 
                    continue
            else:
                print(0)
                break