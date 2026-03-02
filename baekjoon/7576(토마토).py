'''
M x N 배열의 상자에서 3가지의 상태가 표시 됨
1 : 익은 토마토
0 : 익지 않은 토마토
-1 : 아무것도 담겨있지 않음.

토마토가 익을 때 까지의 최소 날짜를 찾아서 출력하는 코드 작성

* 최소 시간 = bfs
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, m, box):
    q = deque()                       # 덱을 받고 시작(시작점은 이번에는 없음)

    for r in range(m):                 # m x n 배열의 상자에서
        for c in range(n):
            if box[r][c] == 1:        # 익은 토마토를 발견한다면 큐에 그 위치를 넣고 그곳에서 시작
                q.append((r, c))

    dr = [-1, 1, 0, 0]               # 상하좌우의 델타 이동 방향을 설정
    dc = [0, 0, -1, 1]

    while q:                         # 큐의 범위 이내에서 
        r, c = q.popleft()           # popleft를 통해 현재의 위치 r, c 값을 뽑는다(시작점)
        for i in range(4):          # 델타 이동을 할 경우의 방향을 설정
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < m and 0 <= nc < n and box[nr][nc] == 0:  # 새로운 위치가 박스 범위 이내이며, 새로운 위치가 익지 않은 토마토일 때
                box[nr][nc] = box[r][c] + 1               # 새로운 위치의 토마토는 하루 뒤에 익을 예정 -> 따라서 1 더하기
                q.append((nr, nc))                # 새로운 위치에서 탐색 계속
  

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]

bfs(n, m, box)       # bfs 함수에 받은 내용들 입력

max_day = 0         # 최대 일수를 0으로 임시 설정
for row in box:     # 박스의 행이 대해서
    if 0 in row:    # 만약 아직도 안 익은 토마토가 있다면
        print(-1)    # 다 익는데 실패했으므로 -1 출력
        exit()       # 종료
    max_day = max(max_day, max(row))  # 2차원 배열의 행 중 가장 큰 값을 찾아서 업데이트 하기 위해

print(max_day-1)
