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

def bfs(start):
    global count
    q = deque([start])
    visited[start] == 1

    while q:
        current = q.popleft()
        for next_node in graph[current]:
            if visited[next_node] == 0:
                count += 1
                visited[next_node] = count
                q.append(next_node)


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

bfs(1)
print(count)