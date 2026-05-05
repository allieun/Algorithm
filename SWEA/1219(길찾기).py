'''
문제 지시사항
    - A에서 출발해서 B로 가는 길이 존재하는지를 확인하는 코드 작성
    - 갈림길은 최대 2대이며, 되돌아올 수 없음(일방통행)
    - 모든 길은 순서쌍으로 표시됨
    - 테스트케이스는 10개 제공

활용 알고리즘 : DFS (완전탐색 재귀)

'''
def dfs(current):
    if current == 99:                   # 현재 위치가 99라면 True반환
        return True
    visited[current] = True             # 현재 위치는 방문 처리
    for next_node in graph[current]:    # 다음 노드를 방문한 적이 없다면 그 노드로 깊이 탐색 실시
        if not visited[next_node]:      # 99를 찾는다면 True 반환
            if dfs(next_node):
                return True
    return False                        # 갈 수 있는 모든 길을 갔는데도 99가 없다면 False 반환


t = 10

for tc in range(1, t+1):
    n, m = map(int, input().split())
    path = list(map(int, input().split()))

    graph = [[] for _ in range(100)]        # 간선 정보를 저장할 빈그래프(간선 범위는 0부터 99까지)
    visited = [False] * 100                 # 방문 여부를 확인할 그래프 추가 (역시 범위는 0부터 99까지)

    for i in range(0, len(path), 2):
        a = path[i]
        b = path[i+1]
        graph[a].append(b)

    if dfs(0):              # 0에서 시작해서 99까지 도착할 수 있다면 1 반환
        answer = 1
    else:                   # 그렇지 않다면 0 반환
        answer = 0

    print(f'#{tc} {answer}')