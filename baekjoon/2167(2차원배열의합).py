'''
델타 및 2차원 배열 연습해보는 문제 추가 풀이
(i, j) 위치부터 (x, y) 위치까지 저장되어있는 수들의 합을 구하는 문제 풀어보기

첫번째로 배열의 크기가 주어지고 n, m과 그 수로 이루어진 배열이 주어짐
합을 구분할 부분의 개수 k
k 줄 만큼 i, j, x, y가 주어진다 (i, j) 부터 (x, y) 까지 범위의 합을 구하는 것

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. 누적 합 배열 생성
dp = [[0] * (m + 1) for _ in range(n + 1)]
for r in range(1, n + 1):
    for c in range(1, m + 1):
        dp[r][c] = grid[r-1][c-1] + dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1]

# 2. 질의 처리
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    # O(1) 만에 답 도출!
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])