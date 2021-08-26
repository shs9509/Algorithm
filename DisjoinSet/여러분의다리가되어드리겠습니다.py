#https://www.acmicpc.net/problem/17352
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(a): # a 노드의 부모 노드 찾기
    if a == parents[a]: # a 노드가 부모 노드이면 a 반환
        return a
    p = find(parents[a]) # a 노드를 따라가면서 부모 노드 찾기
    parents[a] = p # 부모 테이블 갱신
    return parents[a]

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parents[b] = a

n = int(input())
parents = [i for i in range(n+1)]

for j in range(n-2):
    n, m = list(map(int, input().split()))
    union(n, m)

first = find(1)
for i in range(2, n+1):
    if find(i) != first:
        print(1, i)
        sys.exit(0)

        # [0,1,2,3,4] => [1,2] => [0,1,1,3,4] => [1,3] =>[0,1,1,1,4]
        # [0, 1,2,3,4,5] => [1,2] => [0,1,1,3,4,5] => [2,3] => [0,1,1,1,4,5] => [4,5] => [0,1,1,1,4,4] 