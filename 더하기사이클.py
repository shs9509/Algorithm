#문제 https://www.acmicpc.net/problem/1110

number = input()
next_number= int(number)
count =0
number= int(number)
while True:

    if(number)>=10:
        (a,b) = divmod(number,10)
        number = 10*b + ((a+b)%10)
        count += 1
    else:
        number=number*10+number
        count += 1

    if next_number == number:
        break
    
print(count)

# divmod를 알아야 더 간단하다. 
# recursive를 생각했었지만 whlie문이 훨씬 쉬었다.

