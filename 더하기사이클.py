#문제 https://www.acmicpc.net/problem/1110

number = input()    
first_number= int(number)   #초기값
count =0    #반복횟수
number= int(number)
while True: #break를 만날때까지 반복

    if(number)>=10:
        (a,b) = divmod(number,10)   #a는 몫 ,b는 나머지
        number = 10*b + ((a+b)%10)
    else:
        number=number*10+number #한자리경우 10으로 나눌 필요가없다.
    count += 1  #반복횟수 증가

    if first_number == number:  #초기값과 같다면 반복을 빠져나온다.
        break
    
print(count)


