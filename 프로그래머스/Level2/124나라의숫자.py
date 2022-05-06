# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    value=''
    while(n):
        if(n%3):
            value+=str(n%3)
            n=n//3
        else:
            value+='4'
            n=n//3
            n-=1

    return value[::-1]