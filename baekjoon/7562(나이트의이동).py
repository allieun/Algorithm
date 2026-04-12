'''
체스판에서 나이트가 상하좌우를 제외한 각각의 대각선 8방향으로 움직일 수 있을 때, 
몇 번을 움직여야 이동하고자 하는 칸으로 움직일 수 있을까?
'''

import sys
from collections import deque
input = sys.stdin.readline

# 나이트의 8방향 움직임
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    # 함수 내부에서 입력을 직접 받는 식으로 구성하면 가독성이 좋습니다.
    size = int(input())
    sr, sc = map(int, input().split())
    tr, tc = map(int, input().split())

    if sr == tr and sc == tc:
        return 0

    q = deque([(sr, sc)])
    # l 대신 size를 사용하여 숫자 1과의 혼동을 방지
    dist = [[-1] * size for _ in range(size)]
    dist[sr][sc] = 0

    while q:
        cr, cc = q.popleft()
        
        if cr == tr and cc == tc:
            return dist[cr][cc]

        for i in range(8):
            nr, nc = cr + dr[i], cc + dc[i]
            
            if 0 <= nr < size and 0 <= nc < size and dist[nr][nc] == -1:
                dist[nr][nc] = dist[cr][cc] + 1
                q.append((nr, nc))
    return 0

t = int(input())
for _ in range(t):
    print(bfs())