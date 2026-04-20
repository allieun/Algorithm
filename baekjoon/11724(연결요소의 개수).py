'''
방향 없는 그래프가 주여졌을 때, 연결요소의 개수를 구하는 프로그램

연결된 간선의 개수가 아니라 연결된 요소의 개수를 구하는 것이기 떄문에 기존 dfs 노드 갯수 세는 것과는 조금 다른 접근법 필요

DFS 활용한 풀이를 사용하면 괜찮을 듯 하다.
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(current):
    visited[current] = 1                # current를 1(True=방문처리)로 작성하는 이유? -> 1부터 시작하는데, 1은 이미 방문이기 때문
    for next_node in graph[current]:
        if not visited[next_node]:      # 다음 노드가 방문처리 되어있지 않다면 dfs로 재귀처리
            dfs(next_node)              # -> 한 번 DFS 시작 시 정점이 속한 연결 요소 전체가 방문처리


n, m = map(int, input().split())        # n = 정점의 개수, m = 간선의 개수
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)                   # 방문처리할 개수와 연결된 요소들 셀 변수 지정
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):     
    if not visited[i]:      # i 가 방문이 되어있지 않다면 카운트 횟수에 1 추가
        count +=1           # 그리고 이 경우에 dfs 수행
        dfs(i)

print(count)