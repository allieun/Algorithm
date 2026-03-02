'''
우주 괴물 문제의 응용 버전 -> 만약 괴물이 1마리가 아니라 여러마리라면?
1. 괴물의 위치를 먼저 찾아서 리스트에 저장
2. 각 괴물의 위치마다 델타를 이용해 4방향 직선으로 스캔
'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    monsters = []                          # 괴물들의 위치를 찾아서 저장할 빈 리스트
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 2:            # 괴물이 있는 위치의 갑이 2 이기 때문에
                monsters.append((r, c))

    for r, c in monsters:                 # 괴물 위치가 담긴 리스트에서 델타 이동을 통한 사방 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            while 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 1:
                    break
                if grid[nr][nc] == 0:
                    grid [nr][nc] = -1


                nr += dr[i]              # 탐색 중 괴물이거나 (값이 2), 이미 바뀐 범위(다른 괴물의 공격범위)는 통과
                nc += dc[i]
    
    count = 0
    for row in grid:
        count += row.count(0)
    
    print(f'#{tc} {count}')