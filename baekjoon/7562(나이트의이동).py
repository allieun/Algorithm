'''
체스판에서 나이트가 상하좌우를 제외한 각각의 대각선 8방향으로 움직일 수 있을 때, 
몇 번을 움직여야 이동하고자 하는 칸으로 움직일 수 있을까?
'''

import sys
from collections import deque
input = sys.stdin.readline

dr = [-2, -1, 1, 2, 1, 2, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(l, start_r, start_c, target_r, target_c):
    q = deque([(start_r, start_c)])
    dist = [[-1]*l for _ in range(l)]
    dist[start_r][start_c] = 0

    while q:
        current_r, current_c = q.popleft()
        if current_r == target_r and current_c == target_c:
            return dist[current_r][current_c]

        for i in range(8):
            nr = current_r + dr[i]
            nc = current_c + dc[i]
            if 0 <= nr < l and 0 <= nc < l and dist[nr][nc] == -1:
                dist[nr][nc] = dist[current_r][current_c] + 1
                q.append((nr, nc))


t = int(input())
for _ in range(t):
    l = int(input())
    start_r, start_c = map(int, input().split())
    target_r, target_c = map(int, input().split())

    result = bfs(l, start_r, start_c, target_r, target_c)

    print(result)