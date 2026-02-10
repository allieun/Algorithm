t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    w_list = list(input())
    words = list(input())

    i, j = 0, 0

    while i < n and j < m:
        if words[j] == w_list[i]:
            j += 1
            if j == m:
                answer = i
                break
            else:
                answer = -1
        i += 1

    
    print(f'#{tc} {answer}')
