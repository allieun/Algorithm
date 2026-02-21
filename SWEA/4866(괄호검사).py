'''
2 가지의 괄호가 제대로 짝을 이루었는지 검사하는 코드 작성하기
괄호의 종류 : () {}
정상적으로 짝을 이뤘을 경우 1, 그렇지 않다면 0 출력하기

1. 테스트케이스의 범위 안에서 한 줄의 코드를 입력받는다 (진짜 코드 줄이 나옴)
2. 스택은 입력받은 길이만큼으로 지정한다
3. 열린 괄호가 나올 경우 스택에 푸시한다.
4. 입력받은 문자열의 문자가 괄호 ()이나 {}인지 확인
5. 
'''

t = int(input())

for tc in range(1, t+1):
    code = input()                             # 문자열을 입력 받는다
    stack = [0] * len(code)                    # 스택의 길이는 문자열 code의 길이만큼으로 설정
    top = -1                                   # 아직 스택에 채운게 아무것도 없음으로 top 값은 -1
    answer = 1                                 # 정답은 1로 설정(맞았다고 기본적으로 의식)

    for char in code:
        if char in '({':                      # 문자열의 문자들 중 여는 괄호 두 개중 하나에 속한다면
            top += 1                          # 스택에 푸시
            stack[top] = char
        elif char == ')':                          # 만약 문자가 닫는 괄호 ) 일 경우
            if top == -1 or stack[top] != '(':     # 만약 스택에 아무것도 없거나 스택의 top이 여는 괄호 (가 아니라면
                answer = 0                         # 짝이 맞지 않으므로 실패
                break
            else:                                  # 스택에 괄호의 짝이 있을 떄는 푸시
                top -= 1
        elif char == '}':                         # 중괄호 }의 경우도 위와 똑같은 방향으로 진행
            if top == -1 or stack[top] != '{':
                answer = 0
                break
            else:
                top -= 1

    if top != -1:                  # 스택에 아무것도 없지 않다면 실패
        answer = 0

    print(f'#{tc} {answer}')
