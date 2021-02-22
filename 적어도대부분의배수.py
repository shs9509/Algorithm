#https://www.acmicpc.net/problem/1145
arr = list(map(int, input().split()))
def gcd(a,b): #최대 공약수
	if a<b: #a에 더 큰수가 위치해야함
		(a,b) = (b,a)
	while b:
		(a,b) = (b,a%b)
	return a

def gcd(a,b):
    return gcd(b%a,a) if b%a else a 

def lcm(a,b): #최소 공배수
	try:
		return (a*b)//gcd(a,b)
	except:
		return 0
		
ret = 10**6

for i in range(3): #0~2까지와
	for j in range(i+1,4): #i+1부터 4까지와
		for k in range(j+1,5): #j+1 부터 5까지
			ret = min(ret, lcm(lcm(arr[i],arr[j]),arr[k])) #3개의 숫자에 대한 최소 공배수
print(ret)