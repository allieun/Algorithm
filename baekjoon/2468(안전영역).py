'''
지역 높이 정보 파악 -> 비가 왔을 때 물에 잠기지 않는 안전한 영역이 몇 개인지를 찾는다
내리는 비의 양에 따라 일정 높이 이하의 모든 지점이 물에 잠기게 됨

높이 정보는 NxN의 2차원 배열로 주어지며, 각 좌표의 숫자값이 높이를 나타냄
물에 잠기지 않는 영역  = 물에 잠기지 않는 영역이 사방으로 인접해 있고, 그 크기가 최대인 영역

비가 올 때 얼마나 오는지, 어디까지 잠길지는 정해져 있지 않기 때문에 0 부터 최대 높이까지 하니씩 다 시도해본다


'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, rain):
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if not visited[nr][nc] and grid[nr][nc] > rain:
                dfs(nr, nc, rain)



n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_height = 0
answer = 0

for r in range(n):
    for c in range(n):
        max_height = max(max_height, grid[r][c])

for rain in range(max_height+1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and grid[r][c] > rain:
                dfs(r, c, rain)
                count += 1
    answer = max(answer, count)

print(answer)