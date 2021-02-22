#https://www.acmicpc.net/problem/1064
a= list(map(int,input().split()))

b= complex(a[0],a[1])   # b c d 의 점의 좌표를 complex로 표현
c= complex(a[2],a[3])
d= complex(a[4],a[5])

slope =[a[2]-a[0],a[3]-a[1],a[4]-a[0],a[5]-a[1]]    # b-c, b-d 직선의 기울기를 구하기위한 (x,y)좌표들의 차이 

e = abs(b-c)
f = abs(c-d)
g = abs(d-b)    # b, c, d 세점 사이의 거리 e f g


distance=list() # 거리 저장
distance.append(e)
distance.append(f)
distance.append(g)

if e==0 or f==0 or g==0:    # 거리가 다 0! 세점이 같은 자리!
    print(-1)

elif slope[0]==0 and slope[2]==0:   # 거리 두개가 0! 두 점이 같은자리! 
    print(-1)

elif slope[1]==0 and slope[3]==0:   # 거리 두개가 0! 두 점이 같은자리! 
    print(-1)

else:
    while True:
        if 0 in slope:  # x좌표 혹은 y 좌표가 같은 점이 있다. 기울기를 구할때 0이 있으면 곤란하다.
            for i in range(4):
                slope[i] += 1   # 1을 더해줌으로서 방지
        else:
            break

    if (slope[0]/slope[1])==(slope[2]/slope[3]):    #기울기가 같으면 한 직선에 있다는것
        print(-1)

    else:   # 이젠 평행 사변형을 만들수 있다.
        max_dis =max(distance)  # 길이 가장 긴거 2개
        min_dis =min(distance)  # 길이 가장 짧은거 2개
        print( 2*(max_dis-min_dis)) # 빼자