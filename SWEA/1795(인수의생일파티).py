'''
활용 알고리즘 : 다익스트라
'''

import heapq

def dijkstra(start, graph):
    inf = float('inf')
    dist = [inf] * (n+1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)

        if cost > dist[now]:
            continue
        for next_node, weight in graph[now]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    return dist


t = int(input())

for tc in range(1, t+1):
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
        reverse_graph[e].append((s, w))

    go_home = dijkstra(x, graph)
    go_party = dijkstra(x, reverse_graph)

    answer = 0

    for i in range(1, n+1):
        total = go_party[i] + go_home[i]
        answer = max(answer, total)

    print(f'#{tc} {answer}')