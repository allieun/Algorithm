'''
맵의 구성요소

문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)


문자	동작
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

포탄 발사 시 벽돌 벽에 충돌하면 벽이 부서지게 됨, 강철벽은 튕겨나가고 그대로 벽으로 남아있음
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dir_map = {'^' : 0, 'v': 1,'<' : 2, '>' : 3}            # 입력받은 신호를 숫자로
shape_map = {0 : '^', 1 :'v', 2 : '<', 3 : '>'}         # 숫자로 변환한 신호를 다시 문자로
command_map = {'U':0, 'D':1, 'L':2, 'R':3}

t = int(input())

for tc in range(1, t+1):
    h, w = map(int, input().split())
    field = [list(input()) for _ in range(h)]       # 맵 정보 입력받기
    n = int(input())
    command = input()

    r, c, d = 0, 0, 0
    for i in range(h):
        for j in range(w):
            if field[i][j] in dir_map:
                r, c = i, j
                d = dir_map[field[i][j]]
                field[i][j] = '.'
                break
        else:
            continue
        break

    for cmd in command:
        if cmd == 'S':
            nr, nc = r + dr[d], c + dc[d]
            while 0 <= nr < h and 0 <= nc < w:
                if field[nr][nc] == '*':
                    field[nr][nc] = '.'
                    break
                elif field[nr][nc] == '#':
                    break

                nr += dr[d]
                nc += dc[d]
        else:
            d = command_map[cmd]
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < h and 0 <= nc < w and field[nr][nc] == '.':
                r, c = nr, nc

    field[r][c] = shape_map[d]
    print(f'#{tc}', end=' ')
    for row in field:
        print(''.join(row))
