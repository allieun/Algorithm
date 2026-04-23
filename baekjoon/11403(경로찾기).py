'''
가중치가 없는 방향 그래프가 있을 때, 모든 정점에 대해 i에서 j로 가는 길이가 양수인 경로의 여부를 구하는 코드 작성


'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(current, start):
    for next in range(n):
        if graph[current][next] == 1 and result[start][next] == 0:
            result[start][next] = 1
            dfs(next, start)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*n for _ in range(n)]

for i in range(n):
    dfs(i, i)

for row in result:
    print(*row)