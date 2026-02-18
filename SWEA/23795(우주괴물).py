'''
N x N 배열에서 괴물(2)이 상하좌우로 광선을 발사
벽에 막히지만 않는다면 광선은 배열 끝까지 나감
괴물의 위치는 단 한 곳이고, 그 위치의 값은 2이다

1. 테스트 케이스 값과 배열 범위, 그리고 nxn 배열을 차례대로 입력받는다.
2. 배열에서 값이 2인 곳을 찾는다.
3. 광선이 닿지 않는 칸을 카운트할 변수를 지정한다(기본 값은0)
4. 그 값을 기준으로 델타 값을 설정한다. (상하좌우 아마도?)
5. 델타의 범위에서 벽(1)에 닿기 전까지는 공격 범위에 포함되기 때문에 1에 닿는 즉시 반복문 탈출
6. 그 외의 공격범위에 있는 칸들 중 0이라면 그 곳은 공격범위에 포함되기 떄문에 -1로 값을 바꿈
7. 
'''

t = int(input())

for tc in range(1, t+1):
    n= int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 2:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    while 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            break
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = -1

                        nr += dr[i]
                        nc += dc[i]

    count = 0
    for row in grid:
        count += row.count(0)

    print(f'#{tc} {count}')