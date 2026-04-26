import heapq

def dijkstra(start):
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
    return dist[n]


t = int(input())

for tc in range(1, t+1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    result = dijkstra(0)

    print(f'#{tc} {result}')