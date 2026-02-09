'''
1. 길이 n의 리스트와 길이 m의 리스트(n>m)
2. n 범위 안의 리스트 m의 합을 하나하나 구해서 빈 리스트에 추가
3. 인덱스 기준은 m 리스트 가장 왼쪽 (처음엔 둘 다 0, 0에서 시작)
4. 리스트 m의 범위는 (n-m+1) -> 전체 리스트 길이 n에서 m만큼 빠짐
   리스트 길이 10이면 마지막 리스트 m의 인덱스는 7, 8, 9 이기 때문

'''

t = int(input())

for tc in range(1, t+1):
    n, m = map(int,input().split())
    n_list = list(map(int, input().split()))
    sum_list = []

    for i in range(n-m+1):
        num_sum = 0
        for j in range(i, i+m):
            num_sum += n_list[j]
        sum_list.append(num_sum)
    answer = max(sum_list) - min(sum_list)

    print(f'#{tc} {answer}')

