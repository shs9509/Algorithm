# https://programmers.co.kr/learn/courses/30/lessons/72411
def solution(orders, course):
    def comp(li,start,course_len,tmp):
        nonlocal order_set
        if len(tmp)== course_len:
            order_set.add(''.join(tmp))
            return
        for i in range(start, len(li)):
            tmp.append(li[i])
            comp(li,i+1,course_len,tmp)
            tmp.pop() 
    answer =[]
    for length in course:
        order_set = set([])
        for order in orders:
            order = list(order)
            order.sort()
            ''.join(order)
            comp(order,0,length,[])
        
        max_order_count = 0
        best_order_list = []
        for candidate_order_set in order_set:
            count = 0
            for order in orders:
                for menu in candidate_order_set:
                    if menu in order:
                        continue
                    else:
                        break
                else:
                    count+=1    
            if count <2:
                continue
            if count > max_order_count:
                max_order_count = count
                best_order_list = [candidate_order_set]
            elif count == max_order_count:
                best_order_list.append(candidate_order_set)
            else:
                continue
        answer += best_order_list
    answer.sort()
    return answer