'''
N개의 정점과 M개의 간선으로 구성된 무방향 그래프
정점 번호는 1부터 N, 간선 가중치는 1
정점 R에서 시작해서 dfs 탐색으로 노드를 방문할 경우 노드 방문순서 출력 (내림차순)

dfs 1번 문제의 응용 버전
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
    graph[i].sort(reverse=True)

dfs(r)
for g in range(1, n+1):
    print(visited[g])