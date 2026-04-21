'''
알고리즘 캠프에 참여하는 사람 n명
번호는 0번 부터 n-1까지

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.
같은 친구 관계가 있는지? 다 연결되어있는지? 

목표 : 총 5개의 노드로 이루어진 체인이 있는가? (DFS 사용)
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(current, depth):
    if depth == 5:
        print(1)
        exit()
    visited[current] = True
    for next_node in graph[current]:
        if not visited[next_node]:
            dfs(next_node, depth+1)
    visited[current] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [0] * n


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i, 1)

print(0)