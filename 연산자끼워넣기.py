#https://www.acmicpc.net/problem/14888

def cal(count,val,oper):
    if count == num_num:
        ans_li.append(val)
        return
    else: 
        for op in range(4):
            if oper[op]:
                if op == 0:
                    new_val = val+num[count]
                elif op == 1:
                    new_val = val-num[count]
                elif op == 2:
                   new_val = val*num[count]
                elif op == 3:
                    if val <0: # 이거 안해서 틀림
                        new_val = (-val)//num[count]
                        new_val = -new_val
                    else:
                        new_val = val//num[count]
                oper[op] -= 1
                cal(count+1,new_val,oper)
                oper[op] += 1


num_num = int(input()) #2개
num = list(map(int,input().split())) # 5 6
operator_num = list(map(int,input().split())) #  0 0 1 0
# +, -, *, //
ans_li = list() #계산값
cal(1,num[0],operator_num)

print(max(ans_li))
print(min(ans_li))