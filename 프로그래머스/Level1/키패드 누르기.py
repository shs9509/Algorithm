def solution(numbers, hand):
    hand = hand.upper()[0]
    answer=[]
    pos={
        "1":[0,0],
        "2":[0,1],
        "3":[0,2],
        "4":[1,0],
        "5":[1,1],
        "6":[1,2],
        "7":[2,0],
        "8":[2,1],
        "9":[2,2],
        "0":[3,1],
    }
    L=[3,0]
    R=[3,2]
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer.append("L")
            L=pos[str(numbers[i])]
            # print(L)
        elif numbers[i] in [3,6,9]:
            answer.append("R")
            R=pos[str(numbers[i])]
        else:
            x,y = pos[str(numbers[i])] 
            Lx,Ly = L
            Rx,Ry = R
            if abs(Lx-x)+abs(Ly-y)> abs(Rx-x)+abs(Ry-y):
                answer.append("R")
                R=pos[str(numbers[i])]
            elif abs(Lx-x)+abs(Ly-y)== abs(Rx-x)+abs(Ry-y):
                answer.append(hand)
                if hand=="R":
                    R=[x,y]
                else:
                    L=[x,y]
            else:
                answer.append("L")
                L=pos[str(numbers[i])]

    return ''.join(answer)