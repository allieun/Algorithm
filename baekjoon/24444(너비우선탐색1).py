'''
N개의 정점과 M개의 간선으로 이루어진 무방향 그래프에서 bfs 방식으로 노드 탐색을 진행할 경우 노드의 방문순서 출력하기
1. n, m, r(시작정점) 입력
2. m개의 줄에 간선정보 u, v가 주어짐(간선 방향 가중치는 1)
3. bfs 함수를 지정한 뒤 그 안에서 r의 정점에서 출발할 때, 각 노드를 몇 번 방문하는지에 대해 계산 후 출력

'''

from collections import deque                        # 빠른 자료 처리를 위해 덱(deque) 사용은 필수
import sys 
input = sys.stdin.readline

def bfs(start):
    global count                                    # 함수 밖에서 방문 횟수를 의미하는 변수 count를 소환
    q = deque([start])                              # bfs 탐색의 시작점인 start를 덱에 넣은 채로 탐색 시작 (큐 초기화)
    visited[start] = count                          # 시작 정점은 방문 처리 함(탐색에서 맨 처음으로 방문하는 곳이니 방문처리)
    while q:                                        # q 인 동안 = queue 가 빌 때 까지 탐색을 진행 (bfs탐색 기본)
        current = q.popleft()                       # 큐의 맨 앞에 위치한 정점을 pop (first in first out)
        for next_node in graph[current]:            # 그래프에서 현재 위치한 정점과 연결되어있는 정점들을 탐색할 때
            if visited[next_node] == 0:             # 만약 해당 정점에는 방문하지 않았다면 (0 = 방문 x)
                count += 1                          # 방문 횟수 1 추가 
                visited[next_node] = count          # 해당 노드를 몇 번째로 방문했는지를 기록
                q.append(next_node)                 # 큐에 새로 방문한 노드 추가


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]                 # 그래프는 리스트 안에 빈 리스트들이 들어 있는 상태
visited = [0] * (n+1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())             # u와 v = 간선 정보, 1 3 이라면 노드 1에 노드 3이 연결되어있따는 뜻 
    graph[u].append(v)                           # 각 리스트안의 리스트 위치에 해당 하는 노드들을 각각 추가
    graph[v].append(u)

for i in range(1, n+1):                          # 그래프의 각 노드들을 오름차순으로 정렬
    graph[i].sort()

bfs(r)                                          # bfs 탐색 함수를 실행(r은 시작하는 노드)
for i in range(1, n+1):
    print(visited[i])                           # 1번 부터 n번까지 각 노드의 방문 순서를 출력