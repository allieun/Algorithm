'''
1번 컴퓨터가 바이러스에 걸리면 바이러스가 연결되어있는 네트워크를 거쳐 인근 노드를 중심으로 퍼져나간다.
1번 컴퓨터가 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력

1. 컴퓨터의 수 (n) 입력 받음 = 노드 개수
2. 직접 연결되어있는 네트워크의 개수(m) = 간선 개수 
3. m 줄 만큼 네트워크 상에서 연결되어있는 번호쌍 제공 받음

* bfs를 사용해서 풀고 카운트된 개수를 세면 될 것 같음
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):              # 시작 노드를 입력 (아래의 경우에는 1을 입력하게 됨)
    global count             # count 함수를 글로벌로 가져옴
    q = deque([start])       # 큐에 시작지점을 넣고 탐색 시작
    visited[start] = 1       # 시작지점은 방문했기 때문에 1로 바꿔 방문 표시

    while q:             # 큐가 도는 동안 (그러니까 이 범위 안에서)
        current = q.popleft()              # FIFO에 따라 현재 위치 왼쪽에서 꺼내기
        for next_node in graph[current]:   # 현재 위치에서 갈 수 있는 다음 노드들에 대해 
            if visited[next_node] == 0:       # 다음 노드를 방문하지 않았다면
                count += 1                    # 카운트 변수에 1을 추가하고
                visited[next_node] = count    # 다음 노드를 방문으로 변경
                q.append(next_node)           # 큐에 넣어 다음 노드에서 탐색 진행


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)                  # 그래프의 u 인덱스의 리스트에 v 값 넣고, v 인덱스에 u 값 입력
    graph[v].append(u)

for i in range(1, n+1):              # 오름차순으로 그래프 정렬
    graph[i].sort()

bfs(1)
print(count)                         # 최종 카운트된 개수를 정답값으로 출력