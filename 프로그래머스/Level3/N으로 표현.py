def solution(N, number):
    if N == number:
        return 1
        
    s = [ set() for x in range(8) ] 

    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )
    print(s)
    for i in range(1, 8):#1
        for j in range(i):#0
            for op1 in s[j]: #s[0]
                for op2 in s[i-j-1]:#s[0]
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if  number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    print(s)
    return answer