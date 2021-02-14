a= list(map(int,input().split()))

b= complex(a[0],a[1])
c= complex(a[2],a[3])
d= complex(a[4],a[5])

slope =[a[2]-a[0],a[3]-a[1],a[4]-a[0],a[5]-a[1]]

e = abs(b-c)
f = abs(c-d)
g = abs(d-b)


distance=list()
distance.append(e)
distance.append(f)
distance.append(g)

if e==0 or f==0 or g==0:
    print(-1)

elif slope[0]==0 and slope[2]==0:
    print(-1)

elif slope[1]==0 and slope[3]==0:
    print(-1)

else:
    while True:
        if 0 in slope: 
            for i in range(4):
                slope[i] += 1
        else:
            break

    if (slope[0]/slope[1])==(slope[2]/slope[3]):
        print(-1)

    else:
        max_dis =max(distance)
        min_dis =min(distance)
        print( 2*(max_dis-min_dis))