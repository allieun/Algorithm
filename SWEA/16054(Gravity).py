'''
1. 길이가 n인 n_list를 받음
2. 일단 최대 낙차를 0으로 설정
3. 위치 i 부터 n까지의 범위에서 n_list[i]의 값보다 작은 인덱스 값들을 찾아 카운트
4. 최대 낙차값과 비교했을 떄 카운트 된 값이 크다면 최대 낙차값을 카운트 값으로 갱신
5. 리스트를 순회하며 해당 작업 반복
6. 최대 낙차 값을 출력
'''




t = int(input())

for tc in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    max_fall = 0

    for i in range(n):
        count = 0
        for j in range(i+1, n):                             # 이 범위는 전체 범위에서 i를 뺀 범위(차례로 일차원 배열을 순회)
            if n_list[i] > n_list[j]:
                count += 1
        if count > max_fall:
            max_fall = count

    print(f'#{tc} {max_fall}')