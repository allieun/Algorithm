'''
방향성 그래프와 출발, 도착 정점이 주어지면, 경로에 포함된 정점을 한 번만 방문해서 이동 가능한 경로가 몇 개인지 찾는 문제
모든 정점을 지나야 하는 것은 아니다

풀이에 사용할 알고리즘 : DFS
SWEA에서 코드 제출할 때는 sys가 컴파일에러로 처리되니까 빼고 작성할 것
'''
def dfs(current, goal, adj, visited):
    if current == goal:         # 현재 위치와 도착 노드가 같다면 가능한 경로는 1개
        return 1
    visited[current] = True     # 현재 위치 방문처리 (현재 경로에서 해당 노드 사용중이라고 표시)
    count = 0                   # 가능한 경로는1개 count 변수는 0
    for next_node in adj[current]:          # 인접 노드 탐색 (현재 위치 말고 다음 노드)
        if not visited[next_node]:          # 방문한 적이 없다면 다음 노드도 재귀로 dfs 탐색
            count += dfs(next_node, goal, adj, visited)
    visited[current] = False        # 백트래킹: 이 정점을 거쳐가는 모든 탐색이 끝났으므로
    return count                    # 다른 경로에서 이 정점을 다시 사용할 수 있도록 방문 표시를 해제


t = int(input())

for tc in range(1, t+1):
    n, e = map(int, input().split())
    graph = list(map(int, input().split()))     # n : 마지막 정점 번호, e : 간선 수
    s, g = map(int, input().split())            # s : 출발 정점, g : 도착 정점

    adj = [[] for _ in range(n+1)]          # 인접정점 정보 정리할 리스트
    for i in range(0, len(graph), 2):
        u = graph[i]
        v = graph[i+1]
        adj[u].append(v)
    visited = [False] * (n+1)

    answer = dfs(s, g, adj, visited)
    print(f'#{tc} {answer}')