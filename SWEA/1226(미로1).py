'''
16 x 16 배열의 미로에서 출발점(2)에서 도착지(3)까지 도달 가능하다면 1, 아니면 0 출력

1. bfs 탐색을 이용해 문제 풀이(갈림길 탐색 때문에 -> 큐를 통해 모든 길을 다 가보므로 효과적)
2. 델타 이동을 활용해 출발지점인 (1, 1)에서 출발해 목적지점인 3까지 갈 수 있는지를 검사
3. popleft를 활용해 현재 위치의 좌표값을 찾고(First In First Out), 그 좌표값을 기준으로 상하좌우 갈 수 있는 길을 확인
4. 벽이 아니고, 방문한 적이 없다면 다음에 가볼 길로 지정해 큐에 추가
5. 좌표의 값이 3이라면 도달가능한 것이기에 1을 반환
6. 탐색 종료 시까지도 3에 도달하지 못했다면 통과 불가한 미로이므로 0을 반환
'''

from collections import deque

def bfs(start_r, start_c):                # 어디에서 시작하는지에 대한 좌표 값을  입력받아서 처리하는 bfs 함수
    q = deque([(start_r, start_c)])       # 스텍에 탐색을 시작하는 좌표 값을 넣어놓고 시작
    visited[start_r][start_c] = 1         # 시작 좌표는 방문 표시

    dr = [-1, 1, 0, 0]                    # 상하좌우 이동을 델타값으로 표시
    dc = [0, 0, -1, 1]

    while q:                              # 큐가 노드에 남아있는 동안 계속해서 진행됨
        r, c = q.popleft()                # 현재 위치 꺼내기(가장 먼저 발견한 길 - FIFO: First In First Out)
        if grid[r][c] == 3:               # 도착 지점(3)을 찾았을 때
            return 1                      # 미로 탈출 가능하기 때문에 1을 반환
        
        for i in range(4):               # 상하 좌우 주변을 탐색
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < 16 and 0 <= nc < 16:     # 미로의 범위 안에서 해당 위치가 
                if grid[nr][nc] != 1 and visited[nr][nc] == 0:     # 벽(1)이 아니고, 아직 가보지 않은 길이라면
                    visited[nr][nc] = 1               # 방문표시로 바꾸고 
                    q.append((nr, nc))                # 다음 탐색 후보로 큐에 추가
    return 0                               # 만약 모든 길을 다 가봤는데도 도착지에 도달하지 못할 경우 0 반환


t = 10

for tc in range(1, t+1):
    tc = int(input())
    grid = [list(map(int, input().strip())) for _ in range(16)]      # 16 x 16 범위의 미로 입력받음

    visited = [[0]*16 for _ in range(16)]          # 미로의 길 방문 배열 역시 동일한 범위로 설정
    for r in range(16):
        for c in range(16): 
            visited[r][c] = 0                    # 방문시 매번 초기화

    answer = bfs(1, 1)                   # (1, 1)에서 탐색 시작
    print(f'#{tc} {answer}')