'''
치즈와 맞닿아있는 외부공기가 치즈를 녹이게 된다
=> 외부와 연결된 치즈가 어디인지를 파악하는 것이 먼저

[풀이 순서]
1. 좌표 (0,0)은 항상 공기이기 때문에, 여기에서 시작
2. BFS 탐색을 진행 : 값이 0인 곳만 이동 가능, 1인 경우에는 멈춤(치즈이기 떄문)
3. 1과 인접한 좌표의 값은 -1로 변경하거나 visited 배열 활용하기
4. 전체를 순회하면서 외부 공기와 맞닿아있는 치즈를 찾는다
5. 공기와 맞닿아 있는 치즈는 다음 턴에 사라지게 됨 -> 0으로 변경(공기 처리)
6. 사라질 치즈의 개수를 카운트
7. 치즈가 다 사라질 때 까지 반복
'''

import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

time = 0
last_cheese_count = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    visited = [[False]*c for _ in range(r)]
    q = deque([(0, 0)])
    visited[0][0] = True

    melt_cheese = []

    while q:
        current_r, current_c = q.popleft()
        for i in range(4):
            nr = current_r + dr[i]
            nc = current_c + dc[i]
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc]:
                if grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    melt_cheese.append((nr, nc))
                else:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    for melt_r, melt_c in melt_cheese:
        grid[melt_r][melt_c] = 0

while True:
    total_cheese = sum(row.count(1) for row in grid)

    if total_cheese == 0:
        break

    last_cheese_count = total_cheese
    bfs()
    time += 1

print(time)
print(last_cheese_count)