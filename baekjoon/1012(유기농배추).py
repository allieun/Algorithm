'''
n x m 배열의 배추밭에서 1이라고 되어있는 부분에만 심어져있음
배추가 인접해있는 부분이 몇 개인지를 구하는 문제
* 제미나이는 DFS 로 문제를 풀어볼 것을 추천함 * 

1. 배추밭 넓이 n, m을 입력 받은 뒤 해당 배열에 맞춰 배열 생성
2. 그에 맞춰 배추가 심어진 위치를 k만큼 입력(k도 입력받음)
3. 그 이 전에 dfs 함수를 지정해서 상하좌우 한칸씩 이동하며 값이 1인지 탐색하는 과정 정리
4. 테스트 케이스 범위 안에서 dfs를 호출해 배열 안에서 해당 과정 반복
5. 변수 카운트 하며 최종적으로 몇 마리의 지렁이가 필요한지 더한 후 출력
'''
import sys
sys.setrecursionlimit(10000)                      # 에러 방지를 위해 파이썬의 연산 한계 확장
input = sys.stdin.readline

def dfs(r, c, m, n, grid):                         # dfs 방식을 사용해서 풀어봄 (간단한 재귀이기 떄문에)
    grid[r][c] = 0                                 # 현재 칸 방문 처리 (다시 방문하는 중복을 방지하기 위해)

    dr = [-1, 1, 0, 0]                            # 상하좌우 델타 이동방향을 지정해줌
    dc = [0, 0, -1, 1]

    for i in range(4):
        nr = r + dr[i]                            # 현재 위치에서 상하좌우 한칸씩 이동
        nc = c + dc[i]

        if 0 <= nr < m and 0 <= nc < n:
            if grid[nr][nc] == 1:                 # 이동한 칸에 아직 확인하지 않은 배추가 있다면 그 위치로 이동해서
                dfs(nr, nc, m, n, grid)           # 다시 주변 지우기 시작 (재귀)


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())          # 배추가 심어진 위치의 개수
    grid = [[0]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())        # x는 열(column), y는 행(row)
        grid[y][x] = 1                          # 이 위치들은 배열 속에서 배추가 심어진 위치를 나타냄
    
    worm = 0                                    # 벌레가 총 몇 마리 필요한지 셀 변수
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:                  # 만약 이 칸이 방문하지 않은 칸이라면 (여기서 0으로 바뀌면 다시 탐색 안함)
                dfs(r, c, m, n, grid)            # dfs 함수를 활용해 탐색 진행
                worm += 1                        # 함수 카운트 진행
    
    print(worm)