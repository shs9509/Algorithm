n = int(input())
li=[0,1]

for i in range(0,n-1):
  li.append(li[i]+li[i+1])
# print(li)
if n<3:
  print(li[n])
else:
  print(li[-1])  

########################

def p(n):
    x=0
    y=1
    for i in range(n):
        x,y=y,x+y
    return x
a=int(input())
print(p(a))