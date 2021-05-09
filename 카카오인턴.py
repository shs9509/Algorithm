dr = [0,0,-1,1]
dc = [1,-1,0,0]

def search(num,r,c,depth):

    S=[]
    S.append((r,c,depth))
    while S:
        a,b,c = S.pop()
        count =0
        for d in range(4):
            A = a+dr[d]
            B = b+dc[d]
            if 0<=A<5 and 0<=B<5:
                if num[A][B] =='P':
                    if c == 0:
                        return 0
                    elif c== 1:
                        count +=1
                        if count >1:
                            return 0
                elif num[A][B] == 'O':
                    if c== 0:
                        S.append((A,B,c+1))
    return 1


def solution(places):
    result =[]
    for i in range(5):
        flag = False
        for x in range(5):
            for y in range(5):
                if places[i][x][y]=='P':
                    if search(places[i],x,y,0) ==0:
                        result.append(0)
                        flag = True
                        break
            if flag:
                break      
        else:
            result.append(1)
    return result


def solution(s):
    S =list(s)
    one 2 three
    txt=[]
    ans=[]
    for i in S:
        if i not in ['0','1','2','3','4','5','6','7','8','9']:
            txt.append(i)
            # choice(txt,ans)
            if ''.join(txt)=='zero':
                ans.append('0')
                txt.clear()
            elif ''.join(txt)=='one':
                ans.append('1')
                txt.clear()
            elif ''.join(txt)=='two':
                ans.append('2')
                txt.clear()
            elif ''.join(txt)=='three':
                ans.append('3')
                txt.clear()
            elif ''.join(txt)=='four':
                ans.append('4')
                txt.clear()
            elif ''.join(txt)=='five':
                ans.append('5')
                txt.clear()
            elif ''.join(txt)=='six':
                ans.append('6')
                txt.clear()
            elif ''.join(txt)=='seven':
                ans.append('7')
                txt.clear()
            elif ''.join(txt)=='eight':
                ans.append('8')
                txt.clear()
            elif ''.join(txt)=='nine':
                ans.append('9')
                txt.clear()
            else:
                continue
        else:
            ans.append(i)
    return int(''.join(ans))    
    
    
# def choice(num,ans):
#     if ''.join(num)=='zero':
#         ans.append('0')
#     elif ''.join(num)=='one':
#         ans.append('1')
#     elif ''.join(num)=='two':
#         ans.append('2')
#     elif ''.join(num)=='three':
#         ans.append('3')
#     elif ''.join(num)=='four':
#         ans.append('4')
#     elif ''.join(num)=='five':
#         ans.append('5')
#     elif ''.join(num)=='six':
#         ans.append('6')
#     elif ''.join(num)=='seven':
#         ans.append('7')
#     elif ''.join(num)=='eight':
#         ans.append('8')
#     elif ''.join(num)=='nine':
#         ans.append('9')
#     else:
#         return
#     return







〉	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
기댓값 〉	"OOOOXOOO"
실행 결과 〉	실행한 결괏값 "OOOOOXOO"이(가) 기댓값 "OOOOXOOO"와(과) 다릅니다.
테스트 2
입력값 〉	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

def solution(n, k, cmd):
#     k= 현재행수
#     n= 총 행수
    ans =[]
    check=[i for i in range(n)] [0,1,X,3,4,X,6]  [0,1,2,3,4,5,6]
    current_max = n-1
    wait_li = [] #[2,5]
    posit=0
    for c in cmd:
        if c[0] == 'U': #위로가기
            if k-int(c[2]) <= 0:
                k = 0
            else:
                k -= int(c[2])
        elif c[0] == 'D': #아래로 가기
            if k+int(c[2]) >= current_max:
                k = current_max
            else:
                k += int(c[2])
                
        elif c[0] == 'C': #삭제
            check[k] ='X'
            wait_li.append(k)
            if k==current_max:
                k -=1
            current_max -= 1
            
            
        elif c[0]=="Z": #복구
            current_max+=1
            z = int(wait_li.pop(0))
            if k>=z:
                k+=1
            check[z]=z
            
    
    for ch in range(n):
        if ch in check:
            ans.append('O')
        else:
            ans.append('X')
    return ''.join(ans)