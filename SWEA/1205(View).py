'''
1. 리스트의 각 양 끝 2칸씩은 비어있다. 즉 값이 0
2. 인덱스 i 기준 i-2, i-1, i+1, i+2의 값이 2 이상 차이나야 함
3. 그렇다면 위의 4 자리의 값들이 i의 값보다 작으면서 차이까지 2 이상 난다면 괜찮지 않을까?
'''


t = 10

for tc in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    count = 0

    for i in range(2, n-2):
        max_height = max(n_list[i-2], n_list[i-1], n_list[i+1], n_list[i+2])
        if n_list[i] > max_height:
            count += (n_list[i] - max_height)

    print(f'#{tc} {count}')