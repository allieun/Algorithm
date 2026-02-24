'''
단지번호 붙이기 문제 dfs 풀이 방법
'''

import sys
sys.setrecursionlimit(10000)      # 파이썬 연산범위 강제로 늘려주기
input = sys.stdin.readline

def dfs(r, c, n, grid):          # dfs 함수 지정
    grid[r][c] = 0               # 시작은 0(재방문 방지)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    count = 1                    # 일단 단지를 찾았다고 가정(그렇다고 첫 좌표에 아파트가 없어도 카운트되지는 않음)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] == 1:
                count+=dfs(nr, nc, n, grid)
    return count


n = int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]

result = []                          # 단지 번호를 저장할 빈 리스트 생성
for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:          # 이 2차원 배열에서 아파트가 있다면 dfs를 활용해 인근에 아파트가 또 있는지 확인
           result.append(dfs(r, c, n, grid))     #단지를 생성해 단지 번호 리스트에 추가

result.sort()                        # 리스트 정렬 후 단지 개수(리스트 길이), 그리고 줄 바꿔서 리스트 요소들 차례로 출력
print(len(result))
for r in result:
    print(r)


