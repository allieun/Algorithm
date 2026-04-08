'''
G : RC카가 이동 가능한 땅
T : RC카가 이동이 불가능한 나무

X : 현재 RC카의 위치
Y : RC카를 이동 시키고자 하는 위치

<명령어>
A : 앞으로 이동 - 나무가 있는 곳이나 필드를 벗어나는 경우에는 아무 일도 일어나지 않는다.

      (RC카가 망가지는것을 방지하고자 장애물 판단 시스템이 탑재되었다.)
L : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
R : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전

항상 RC카가 위를 바라보는 방향으로부터 조종을 시작

'''

t = int(input())

dr = [-1, 0, 1, 0]        # 상하좌우로 표기하지 않고, 원형 방향으로 표기
dc = [0, 1, 0, -1]        

for tc in range(1, t+1):
    n = int(input())
    field = [list(input()) for _ in range(n)]    # RC카 맵 입력
    start_r, start_c = 0, 0
    for r in range(n):
        for c in range(n):

            if field[r][c] == 'X':
                start_r, start_c = r, c

    q = int(input())
    result = []
    for _ in range(q):
        len_c, command = input().split()
        len_c = int(len_c)
        r, c = start_r, start_c
        d = 0
        for cmd in command:
            if cmd == 'A':
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n and field[nr][nc] != 'T':
                    r, c = nr, nc
            elif cmd == 'L':
                d = (d-1) % 4
            elif cmd == 'R':
                d = (d+1) % 4

        if field[r][c] == 'Y':
            result.append(1)
        else:
            result.append(0)

    print(f'#{tc}', *result)
