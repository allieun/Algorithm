'''
단지번호 붙이기 문제 bfs로 풀어보기
1은 집이 있는 곳, 0은 집이 없는 곳
대각선 상에 집이 있을 경우는 단지로 연결된 것이 아님

'''

import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = True
    count = 1
    while q:
        current_r, current_c = q.popleft()
        for i in range(4):
            nr = current_r + dr[i]
            nc = current_c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    count += 1
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return count

n = int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]* n for _ in range(n)]

result = []

for r in range(n):
    for c in range(n):
        if grid[r][c] == 1 and not visited[r][c]:
            result.append(bfs(r,c))

result.sort()
print(len(result))
for i in result:
    print(i)

