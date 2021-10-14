#https://www.acmicpc.net/problem/1106
from sys import stdin, maxsize


if __name__ == '__main__':
    # 확보해야할 고객, 도시의 수
    C, N = map(int, stdin.readline().split())
    # 광고 정보
    ad = [list(map(int, stdin.readline().split())) for _ in range(N)]
    # 적어도 C명을 늘려야 하기에, 고객의 수 최대 값을 더해 줄 필요가 있음
    dp = [0] + [maxsize] * (C + 100)

    for cost, customer in ad:
        for cur_customer in range(customer, C + 101):
            dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + cost)

    print(min(dp[C:C + 101]))