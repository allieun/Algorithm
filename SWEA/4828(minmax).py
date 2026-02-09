'''
1. 각 리스트의 가장 큰 값과 가장 작은 값을 구함
2. 테스트 케이스 범위 내에서 그 둘의 차이를 구하는 값을 정의한 뒤 테스트 케이스 번호와 함께 출력
'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))

    min_num = min(n_list)
    max_num = max(n_list)
    answer = max_num - min_num

    print(f'#{tc} {answer}')