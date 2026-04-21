'''
n 개의 컴퓨터를 한 번의 해킹으로 연결해서 해킹한다고 할 경우,
가장 많은 개수의 컴퓨터를 해킹할 수 있는 컴퓨터 번호 출력하기 

DFS 풀이

'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(current):
    visited[current] = 1
    count = 1
    for next_node in graph[current]:
        if not visited[next_node]:
            count += dfs(next_node)
    return count 


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

max_count = 0
result = []


for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n+1):
    visited = [0] * (n+1)
    count = dfs(i)

    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

print(*result)
    