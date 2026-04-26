'''
인접 지역으로 이동 시 연료 기본 소모량 1, 더 높은 곳으로 이동할 경우 높이만큼 추가 연료 소모 있음
목표 : 이동 가능한 지역의 높이 정보에 따른 최소 연료 소비량을 구하는 것
활용 알고리즘 : 다익스트라
핵심 포인트
- 
'''
from heapq import heappush, heappop

def dijkstra():
    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dist[0][0] = 0

    pq = []
    heappush(pq, (0, 0, 0))
    
    while pq:
        cost, r, c = heappop(pq)
        if cost > dist[r][c]:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                new_cost = cost + 1
                if graph[nr][nc] > graph[r][c]:
                    new_cost += graph[nr][nc] - graph[r][c]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heappush(pq, (new_cost, nr, nc))

    return dist[n-1][n-1]


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    answer = dijkstra()

    print(f'#{tc} {answer}')