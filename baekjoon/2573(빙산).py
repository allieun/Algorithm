'''
목표 : 하나의 빙산이 두 개로 갈라지는 최초의 시점을 출력하는 것
결론 : 단지번호 붙이기 + 치즈
이걸 단지번호 붙이기 (dfs) + 치즈 (bfs) 의 형태로 구현한다면 더 깔끔한 코드가 나올 것
-> 근데 제미나이의 추천은 dfs + 2차원 배열 순회(델타이동) 이었음
'''

import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def count_ice():
    visited = [[False]*m for _ in range(n)]
    count = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] > 0 and not visited[r][c]:
                count += 1
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    curr_r, curr_c = q.popleft()
                    for i in range(4):
                        nr, nc = curr_r + dr[i], curr_c + dc[i]
                        if 0 <= nr < n and 0 < nc < m and grid[nr][nc] > 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
    return count


def melt_ice():
    melt = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if grid[r][c] > 0:
                water_cnt = 0
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        water_cnt += 1
                melt[r][c] = water_cnt
    for r in range(n):
        for c in range(m):
            grid[r][c] = max(0, grid[r][c] - melt[r][c])


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

time = 0

while True:
    cnt = count_ice()
    if cnt >= 2:
        print(time)
        break
    if cnt == 0:
        print(0)
        break
    melt_ice()
    time += 1