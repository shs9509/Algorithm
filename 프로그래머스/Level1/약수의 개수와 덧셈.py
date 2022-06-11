def solution(left, right):
    answer = 0
    def check_divisor_even(num):
        count_divisor = 0
        for i in range(1,num+1):
            if num%i==0:
                count_divisor+=1
        if count_divisor%2==0:
            return True
        else:
            return False
    
    while(left<=right):
        if check_divisor_even(left):
            answer+=left
        else:
            answer-=left
        left+=1
    return answer

///////////////////////////////////
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer