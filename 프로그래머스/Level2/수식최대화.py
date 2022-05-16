# https://programmers.co.kr/learn/courses/30/lessons/67257
import copy
def operate(oper,num1,num2):
    if oper=="-":
        return num1-num2
    if oper=="*":
        return num1*num2
    if oper=="+":
        return num1+num2
def calc(num_li,operation,order):
    print(order,num_li,operation)
    while(order):
        oper = order.pop(0)
        while(len(num_li)>1):
            # print(num,operation)
            for i in range(len(operation)):
                if operation[i] == oper:
                    operation.pop(i)
                    num1 = num_li.pop(i)
                    num2 = num_li.pop(i)
                    num3 = operate(oper,num1,num2)
                    num_li.insert(i,num3)
                    break 
            else:
                break
    return num_li[0]
def solution(expression):
    expression = list(expression)
    operation=[]
    num=[]
    tmp = []
    answer = []
    for i in range(len(expression)):
        if expression[i] in ['-','+','*']: 
            operation.append(expression[i])
            num_str = ''.join(tmp)
            num.append(int(num_str))
            tmp = []
        else:
            tmp.append(expression[i])
    num_str = ''.join(tmp)
    num.append(int(num_str))
    orders = [['-','+','*'],['-','*','+'],['+','*','-'],['+','-','*'],['*','+','-'],['*','-','+']]
    for order in orders:
        copy_num = copy.copy(num)
        copy_operation = copy.copy(operation)
        answer.append(calc(copy_num,copy_operation,order))
    return max(abs(min(answer)),max(answer))