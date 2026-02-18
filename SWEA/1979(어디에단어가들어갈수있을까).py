'''
N x N의 배열에서 검정색으로 칠해진 칸을 제외했을 때, 길이 k의 단어가 들어갈 수 있는 경우의 수 조사하기

1. 테스트케이스와 배열 범위 n, 단어 길이 k 입력받음
2. n x n 배열의 2차원 리스트 입력받음
3. 행 우선 순회와 열 우선 순회를 진행
4. 행 우선 순회 시 흰색 칸(1)의 갯수를 새어 그 길이가 k와 같을 때, 행 우선 순회 카운트 변수에 포함
5. 열 우선 순회도 위와 동일한 방식으로 진행
6. 최종적으로는 두 경우의 수에 포함된 값들을 모두 더한 결과 값 출력
'''

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]             # 범위가 n x n 인 배열 생성

    answer = 0                                                             # 결과값 변수 지정

    for r in range(n):                                                     # 행 우선 순회 진행
        count_r = 0                                                        # 행 순회 중 가능한 변수 카운트할 변수 지정
        for c in range(n):
            if grid[r][c] == 1:                                            # 행에서 하얀색(1)인 부분 찾아서 카운트
                count_r +=1
            if grid[r][c] == 0 or c == n-1:                               # 검정색 칸(0)을 만나거나, 열 값이 배열의 끝에 다다랐을 때
                if count_r == k:                                          # 카운트 갯수가 단어 길이 k 값과 같다면
                    answer += 1                                           # 정답에 1 추가
                count_r = 0                                               # 다시 카운트 값을 0으로 되돌리고 반복

    for c in range(n):                                                    # 열 우선 순회 진행
        count_c = 0                                                       # 열 우선 순회 중 가능한 변수 카운트할 변수 지정
        for r in range(n):
            if grid[r][c] == 1:                                           # 하얀색 칸(1)을 만났을 때 1씩 카운트 
                count_c += 1
            if grid[r][c] == 0 or r == n-1:                               # 검정색 칸(0)을 만나거나, 행 값이 배열의 끝에 다다랐을 때
                if count_c == k:                                          # 카운트 된 값이 k 값과 같다면
                    answer += 1                                           # 정답에 1 추가
                count_c = 0                                               # 다시 카운트 변수를 0으로 되돌린 뒤 해당 과정 반복

    print(f'#{tc} {answer}')
    