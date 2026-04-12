from collections import deque

# [1] 상수 및 델타 정의 (암기하기 쉬운 순서)
# 우(0), 하(1), 좌(2), 상(3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
move_cmds = ["RA", "DA", "LA", "UA"]
fire_cmds = ["RF", "DF", "LF", "UF"]

# 글로벌 명령어 저장소 (while문 밖에서 선언)
actions = []

# [2] BFS 함수 (한 번만 잘 쳐두면 끝!)
def get_bfs_actions(H, W, map_data, start, target):
    q = deque([(start[0], start[1], [])])
    v = [[False] * W for _ in range(H)]
    v[start[0]][start[1]] = True
    
    while q:
        r, c, path = q.popleft()
        
        # 사거리 3칸 체크 (공격 가능한지 먼저 확인)
        for i in range(4):
            for k in range(1, 4):
                nr, nc = r + dr[i]*k, c + dc[i]*k
                if not (0 <= nr < H and 0 <= nc < W) or map_data[nr][nc] == 'R':
                    break
                if (nr, nc) == target:
                    return path + [fire_cmds[i]] # 경로 + 공격 반환

        # 이동 탐색 (한 칸씩 이동)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < H and 0 <= nc < W and not v[nr][nc]:
                # 평지('G')일 때만 이동
                if map_data[nr][nc] == 'G':
                    v[nr][nc] = True
                    q.append((nr, nc, path + [move_cmds[i]]))
    return []

# ---------------------------------------------------------
# [3] 메인 프로그램 루프 (스켈레톤 코드 안의 핵심 영역)
# ---------------------------------------------------------
while True: # 보통 스켈레톤에 이미 있는 무한 루프
    # (이미 구현되어 있을 데이터 파싱 부분)
    # map_data, my_pos, enemies 등 수신 로직...
    
    # 여기서부터 태은 님이 직접 타이핑할 구간
    H, W = len(map_data), len(map_data[0])
    target_pos = enemies['X'] # 포탑 위치

    # [수정 1] actions가 비어있을 때만 길 찾기 (강사님 강조 포인트)
    if not actions:
        actions = get_bfs_actions(H, W, map_data, my_pos, target_pos)

    # [수정 2] 명령어 하나씩 꺼내기
    if actions:
        output = actions.pop(0)
    else:
        output = "S" # 갈 곳 없으면 대기 (과락 방지용)

    # [수정 3] 결정된 output 전송 (보통 이미 있는 코드)
    # submit(output)