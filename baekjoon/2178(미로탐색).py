'''
N x M 배열로 표현되는 미로에서 좌표 (n, m)으로 이동할 때까지의 최소 칸 수를 구하는 코드 작성
시작은 (1, 1)에서 출발하며 이동시 인접 칸으로만 이동 가능
칸의 값이 1일 때만 이동할 수 있음 (칸 셀 때는 시작 위치와 도착위치도 포함)

활용할 탐색 방법: bfs

1. n, m 입력 받음
2. n 개의 줄에 m개의 정수로 미로 주어짐
3. 
'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, m, grid):
    q = deque([(0, 0)])        # 큐에 시직 위치인 (0, 0)을 넣고 시작

    dr = [-1, 1, 0, 0]         # 델타이동을 상하좌우로 설정
    dc = [0, 0, -1, 1]

    while q:                   # 큐가 빌 때 까지 반복하는 과정 
        r, c = q.popleft()     # 현재 위치는 FIFO에 따라 왼쪽에서 뽑아옴
        for i in range(4):     # 델타 이동에 따라 현재 위치에서 4방향 탐색
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:        # 미로의 전체 범위를 벗어나지 않는지 확인
                if grid[nr][nc] == 1:              # 현재 방문하지 않았으며, 이동가능한 길(1)이라면
                    grid[nr][nc] = grid[r][c] + 1     # 현재 위치까지의 거리 + 1(처음 방문하는 순간이 최단거리이기 때문)
                    q.append((nr, nc))             # 다음 탐색을 위해 해당 위치를 큐에 추가
    
    return grid[n-1][m-1]            # 도착지점에 저장된 값이 최단 거리(-1을 하는 이유는 인덱스가 0부터 시작하기 때문)

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(n, m, grid))
