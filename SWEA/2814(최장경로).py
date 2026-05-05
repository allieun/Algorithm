'''
문제 조건
    - N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프의 최장경로 길이 계산
    - 시작점이 주어져 있지 않기 때문에 어디서 시작해도 다 괜찮음
    - 번호는 1번 부터 N번까지 순서대로 부여됨
    - 같은 정점의 번호가 두 번 이상 등장할 수 없음

활용할 알고리즘 : 
'''

def dfs(start, dist):
    global max_len                  # 최장 길이 변수 호출
    if dist > max_len:              # 길이가 최장 길이보다 길면 그걸 최장길이로 교체
        max_len = dist
    visited[start] = True           # 시작 노드 방문 처리
    for next_node in graph[start]:      # 다음 노드에 대해서 방문하지 않았다면 dfs에 넣어서 깊이 탐색 실시
        if not visited[next_node]:
            dfs(next_node, dist+1)
    visited[start] = False          # 방문기록 지우는 이유 : 다른 시작점에서 출발할 경우 이 노드 다시 사용 가능
                                    # 최장경로를 찾으려면 여러 다양한 정점에서 출발해서 탐색하는게 필요하기 때문


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)                  # 양방향 그래프이기 때문에 둘 다 그래프에 추가
        graph[y].append(x)
    
    max_len =0

    for i in range(1, n+1, 2):             # 2개씩 묶어서 분류
        visited = [False]*(n+1)            # 방문 여부 확인 그래프 제작
        dfs(i, 1)                           # i = 시작하는 노드, 1은 현재의 거리
    
    print(f'#{tc} {max_len}')