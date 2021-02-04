import sys
while True:
    a=sys.stdin.readline()
    if a=="0\n":       #readline()은 개행처리하기 떄문에 '\n' 이 포함된다.
        break
    else:
        if int(a) == int(a[::-1]): #[::-1]로 순서를 뒤바꾸어 줬다.
            print('yes')
        else:
            print('no')
