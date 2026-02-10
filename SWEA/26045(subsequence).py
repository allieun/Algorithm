'''
수열 A와 B는 1 이상 9 이하의 정수로 구성 될 때 B가 A의 부분수열인지의 여부 판별하기
상대적인 순서는 일치해야 한다는 점 명심하기
n은 수열 A의 길이, B는 수열 B의 길이
리스트 두 개를 차례대로 입력받음
리스트 a와 b를 각각 순회하면서 순서대로 리스트 b의 요소가 a에도 들어있는지 확인하기
들어있다면 인덱스 번호 +1을 하면서 리스트 b와 리스트 a를 순회
만약 리스트 b의 인덱스 j의 값이 리스트 a에 없다면 거기에서 stop

j 값이 m 값과 같은 경우는 정답, 아니면 오답

'''

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    i, j = 0, 0                                 # i = a_list의 인덱스, j = b_list의 인덱스

    while i < n and j < m:                      # a_list와 b_list를 다 돌았는지의 여부 확인
        if b_list[j] == a_list[i]:
            j += 1
        i += 1

    if j == m:
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'#{tc} {answer}')