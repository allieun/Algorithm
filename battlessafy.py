from collections import deque

# 1. 고정 변수 및 델타 정의 (가이드라인 준수)
# DIRS: 0:우, 1:하, 2:좌, 3:상
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
MOVE_CMDS = {0: "RA", 1: "DA", 2: "LA", 3: "UA"}
FIRE_CMDS = {0: "RF", 1: "DF", 2: "LF", 3: "UF"}

START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = 'R'

# 글로벌 명령어 저장소
actions = []

# ---------------------------------------------------------
# 2. 핵심 로직: BFS 함수 (경로 구하기)
# ---------------------------------------------------------
def get_bfs_actions(H, W, map_data, start_pos, target_pos):
    """현재 위치에서 목표 사거리까지의 명령어 리스트(actions)를 반환"""
    q = deque([(start_pos[0], start_pos[1], [])])
    visited = [[False] * W for _ in range(H)]
    visited[start_pos[0]][start_pos[1]] = True
    
    while q:
        r, c, path = q.popleft()
        
        # [A] 사거리 체크: 현재 위치에서 타겟이 사거리 3 이내에 있는가?
        for i in range(4):
            dr, dc = DIRS[i]
            for k in range(1, 4):
                nr, nc = r + dr * k, c + dc * k
                if not (0 <= nr < H and 0 <= nc < W): break
                if map_data[nr][nc] == WALL_SYMBOL: break # 바위는 시야 차단
                
                if (nr, nc) == target_pos:
                    # 사거리 진입 성공! 이동 경로 + 발사 명령 반환
                    return path + [FIRE_CMDS[i]]

        # [B] 이동 탐색: 4방향으로 한 칸씩 이동 (땅 'G'만 가능)
        for i in range(4):
            nr, nc = r + DIRS[i][0], c + DIRS[i][1]
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                # 이미지 정보에 따라 'G'(풀)만 이동 가능으로 설정
                if map_data[nr][nc] == 'G':
                    visited[nr][nc] = True
                    # 명령어(예: 'RA')를 path 리스트에 추가하며 탐색
                    q.append((nr, nc, path + [MOVE_CMDS[i]]))
                    
    return [] # 경로가 없는 경우

# ---------------------------------------------------------
# 3. 메인 프로그램 (연결 및 무한 루프)
# ---------------------------------------------------------
def main():
    global actions
    # (이미 구현되어 있을 부분: 초기화 및 연결)
    # connect_to_server() 

    while True:
        # [수정 포인트 1] 입력 데이터 수신 및 변수 할당
        # game_data = receive_data() 
        # map_data, my_pos, enemies, codes 등 파싱
        
        # 가이드대로 적 포탑(X)의 좌표 가져오기
        target_pos = enemies['X'] 
        H = len(map_data)
        W = len(map_data[0])

        # [수정 포인트 2] actions가 비어있을 때 BFS 리필 (강사님 핵심 로직)
        if not actions:
            actions = get_bfs_actions(H, W, map_data, my_pos, target_pos)

        # [수정 포인트 3] 명령어 하나씩 전송 및 갱신
        if actions:
            output = actions.pop(0) # 하나씩 꺼내기
        else:
            output = "S" # 경로가 없거나 할 일 없으면 대기

        # 명령어 전송 및 터미널 출력
        # send_command(output)
        # print(f"Current Action: {output}")

        # (이미 구현되어 있을 부분: game_data 업데이트 대기)