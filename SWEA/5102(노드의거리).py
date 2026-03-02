'''
노드의 개수 v개, 방항성 없는 e개의 간선 정보
출발 노드가 주어졌을 때, 최소 몇 개의 간선을 지나야 도착노드에 도달할 수 있을지 알아내기
노드번호는 1번 부터 존재함

'''
from collections import deque

def bfs(s, g, graph):        # bfs에 시작점과 도달점, 그리고 그래프에 대한 정보를 넣고 시작
    q = deque([s])           # 큐에 시작점을 넣고 시작
    visited[s] = 1           # 시작점은 방문처리

    while q:
        current = q.popleft()      # FIFO 규칙에 따라 큐에서 현재 지점을 꺼냄
        if current == g:             # 현재 위치가 목표지점일 때는 현재 기록된 거리 반환
            return visited[current] - 1     # 시작점을 1로 잡았으므로 실제 간선 개수를 위해 1을 빼줌
        for next_node in graph[current]:     # 현재 노드의 위치에서 탐색 가능한 다음 노드들 중
            if not visited[next_node]:       # 아직 방문하지 않았다면 
                visited[next_node] = visited[current] + 1          # 이전 노드까지의 거리 + 1을 다음 노드에 기록
                q.append(next_node)

    return 0                   # 탐색이 불가능할 경우 0 반환


t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    s, g = map(int, input().split())
    answer = bfs(s, g, graph)

    print(f'#{tc} {answer}')