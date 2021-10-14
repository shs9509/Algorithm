# https://www.acmicpc.net/problem/16916

# test = input()
# part = input()
# if part in test:
#     print(1)
# else:
#     print(0)

def getPI(pattern):# aek
    j = 0
    for i in range(1, len(pattern)): # 1부터 3까지
        while j > 0 and pattern[i] != pattern[j]: #  j=1, e!= e
            j = pi[j - 1] # 
        if pattern[i] == pattern[j]: #  a==a
            j += 1 # j=1
            pi[i] = j #  pi =[0]

def KMP(s, pattern):
    getPI(pattern)# [0,0,0]
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False
# baekjoon
# aek
s = input() # baekjoon
pattern = input() # aek
pi = [0 for x in range(len(pattern))]
# [0,0,0]

if KMP(s, pattern):
    print('1')
else:
    print('0')