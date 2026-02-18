'''
크기가 n 인 파스칼의 삼각형 만들기 문제
[규칙]
(1) 첫 번째 줄은 항상 숫자 1이다.
(2) 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

1. 일단 맨 위가 1로 채워진 리스트에서 시작해도 될 듯 하다.
2. 양 끝은 항상 1이라는 사실을 기억해야 한다.
3. n 을 입력받은 후 일단 1차원 배열에서 맨 윗단이 채워진 리스트를 하나 생성한다
4. 그 리스트를 제외한 n의 범위에서 이전 리스트의 값을 가져오는 변수를 설정한다.
5. 
'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    pascal = [[1]]

    for i in range(1, n):
        prev = pascal[-1]
        new_pascal = [1]

        for j in range(len(prev)-1):
            new_pascal.append(prev[j] + prev[j+1])
        new_pascal.append(1)
        pascal.append(new_pascal)

    print(f'#{tc}')
    for row in pascal:
        print(*row)