import sys
while True:
    a=sys.stdin.readline()
    # print(type(a),a)
    if a=="0\n":
        break
    else:
        if int(a) == int(a[::-1]):
            print('yes')
        else:
            print('no')

