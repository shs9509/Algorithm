a = input()
a = int(a)

count =0
while a!=0:
    if not a%2:
        a = a/2
    else:
        a = a//2
        count += 1
print(count)