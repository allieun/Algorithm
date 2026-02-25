'''
N 개의 정점과 M개의 간선으로 구분된 무방향 그래프
정점 번호는 1부터 N번이고 모든 간선의 가중치는 1
정점R에서 시작해 깊이 우선 탐색(dfs)으로 노드를 방문할 경우의 방문순서 출력하기

그래프형 dfs 문제를 풀어보자!

1. n, m, r 입력 후 m줄만큼 u, v를 입력받는다
2. 그래프 문제이기 때문에 visited 리스트를 활용해서 풀어보자
3. 
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(current):
    global order
    visited[current] = order
    for next_node in graph[current]:
        if visited[next_node] == 0:
            order += 1
            dfs(next_node)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
order = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

dfs(r)
for i in range(1, n+1):
    print(visited[i])
