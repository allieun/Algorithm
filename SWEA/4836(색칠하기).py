'''
격자 판 배열은 10 x 10
빨간색은 1, 파란색은 2로 구분 -> 둘이 더한 3의 값을 가지는 인덱스가 있다면 보라색으로 구분
완전탐색을 기반으로 문제 풀이

1. 10 x 10 배열의 격자에 모두 0을 넣는다. 범위는 0부터 9까지가 됨
2. 보라색 칸수를 계산할 변수 하나 추가(시작값은 0)
3. n의 횟수 만큼 r1, c1, r2, c2, color 입력받는다
4. r1 부터 r2의 범위 그리고 c1부터 c2의 범위에서 각각 입력받은 숫자 입력
5. 종료 후 전체 배열을 완전 탐색하면서 해당 인덱스 값이 3이면 보라색 칸수 계산 변수에 1추가
'''
t = int(input())

for tc in range(1, t+1):
    n = int(input())                           # n은 칠할 영역의 개수
    grid = list([0]*10 for _ in range(10))     # 10 x 10의 배열이 생기고, 안에는 다 0으로 차있다

    purple = 0

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())    # n 번 만큼 색칠할 좌표 및 정보 입력받기

        for r in range(r1, r2+1):                  # 여기에서 r2에 1을 더하는 이유는 범위 끝 수는 포함 안되서 실제로는 r2-1까지만 이라서
            for c in range(c1, c2+1):              # c2도 마찬가지
                grid[r][c] += color                # 해당 그리드 위치에 컬러 색으로 칠(1 = red, 2 = blue)

    for r in range(10):                            # 전체 리스트를 순회하면서 혹시 그리드 값이 3이라면 purple 변수에 1씩 더한다
        for c in range(10):
            if grid[r][c] == 3:
                purple += 1

    print(f'#{tc} {purple}')
