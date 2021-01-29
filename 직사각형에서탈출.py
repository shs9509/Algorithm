position = input()
position=position.split(' ')
x=int(position[0])
y=int(position[1])
w=int(position[2])
h=int(position[3])
if x>(w-x):
    x=w-x
if y>(h-y):
    y=h-y

if x>y:
    print(y)
else:
    print(x)
