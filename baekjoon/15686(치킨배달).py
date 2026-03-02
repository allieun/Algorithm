'''
N x N 의 배열에서 치킨집은 2의 값을, 집은 1의 값을 가짐(0은 그냥 빈칸)
치킨집과 집 사이의 거리는 절대값으로 계산
동네에 치킨집이 여러개 있을 경우 집 기준 더 가까운 곳으로 치킨거리를 계산
동네 최적의 치킨집 개수 m개를 구해야 함 -> 전체를 다 탐색해야 하기 때문에 DFS 방식을 활용하는 것이 적절

최적의 치킨집 개수 = 가장 작은 치킨 거리의 합(가장 적은 치킨집으로 최고의 수익을 낸다)

1. 치킨집의 위치와 가정집의 위치를 따로 받아서 저장
2. 전체 치킨집 리스트에서 m개를 뽑는 모든 경우의 수를 DFS로 구한다 (중복 없이 -> 백트래킹 활용)
3. 각 치킨집에서 각각의 집들 과의 맨해튼 거리를 구한다 (맨해튼 거리 : 절대값 거리)
4. 각 조합마다 거리 값들의 합의 최솟값을 구하고, 각각 비교해서 더 작은 값으로 갱신
'''

import sys
input = sys.stdin.readline
                                                  # count = 현재 select에 몇 개의 치킨 값을 골랐는지를 나타내는 변수
def dfs(idx, count):                              # idx = 다음에 고를 치킨집 후보를 어느 인덱스 부터 볼지 (중복방지)
    global answer                                 # answer 변수를 함수 밖에서 가지고 옴(일단은 매우 큰 수)
    if count == m:                                # 치킨집을 m 개를 다 골랐을 경우
        total_dist = 0                            # total_dist = 모든 집에 대해 가장 가까운 치킨집까지의 거리를 더한 값
        for hr, hc in house:                      # house 리스트 안에 들어있는 집의 좌표들 (hr, hc)에 대해 
            temp_min = float('inf')               # float('inf') -> 무한대로 설정해서 앞으로 쭉 더 작은 값으로 갱신
            for cr, cc in select:                 # 현재 dfs가 뽑아둔 치킨집의 좌표(cr, cc) 중에서 선택된 치킨집에 대해
                dist = abs(hr-cr) + abs(hc-cc)       # 거리는 멘해튼 거리로 구하기 위해 abs 사용
                temp_min = min(temp_min, dist)       # 가장 작은 거리를 갱신(맨해튼 거리와 최소 거리 변수 중 더 작은것 선택)
            total_dist += temp_min                  # 해당 집과 치킨집과의 최소 거리 누적
        answer = min(answer, total_dist)            # 지금 조합에서의 치킨 거리 합과 기존이 answer 값 비교해서 더 작은 값 선택
        return

    for i in range(idx, len(chicken)):           # 만약 m 개를 다 고르지 못했을 경우 백트래킹을 통해 조합 만들어가기
        select.append(chicken[i])                # select에 치킨집 위치 i번을 넣고
        dfs(i+1, count +1)                       # 다음 단계로 이동해 i+1부터 탐색(중복방지)
        select.pop()                             # 탐색 종료 후 원상복구


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]    # 마을 지도

house = []                 # 집 위치를 모을 리스트
chicken = []               # 치킨집 위치를 모을 리스트

for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            house.append((r, c))
        elif grid[r][c] == 2:
            chicken.append((r, c))

answer = float('inf')
select = []

dfs(0, 0)
print(answer)