t = int(input())

for tc in range(1, t+1):
    n = int(input())
    grid = list([0]*10 for _ in range(10))
    purple = 0

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                grid[r][c] += color

    for r in range(10):
        for c in range(10):
            if grid[r][c] == 3:
                purple += 1

    print(f'#{tc} {purple}')