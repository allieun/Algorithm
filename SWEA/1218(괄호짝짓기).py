'''
테스트 케이스 10개 중에서 괄호 짝이 지어진 경우는 1, 아닌 경우는 0으로 표사
괄호 문자 종류는 4종 (), {}, [], <>

1. 일단 테스트케이스 범위 안에서 문자열을 입력 받는다.
2, 스택을 생성하는데, 스택의 길이는 입력받은 문자열의 길이만큼으로 지정한다.
3. 여는 괄호가 나올 때 마다 스택에 푸시
4. 만약에 닫는 괄호가 나온다면 스택에서 하나를 pop 해서 닫는 괄호와 짝이 맞는지 확인
5. 만약 최종 스택의 top 값이 -1이 아닐 경우에는 짝지어지지 않았다는 의미이기 때문에 0 출력
6. 그 외에도 스택에서 팝한 문자와 검사를 했을 때 짝이 지어지지 않는다면 이 경우에도 반복문 멈추고 0 출력
'''

t = 10

for tc in range(1, t+1):
    len_char = int(input())
    character = input()
    stack= [0]*len_char
    top = -1
    answer = 1

    for char in character:
        if char in '({[<':
            top += 1
            stack[top] = char
        elif char in ')}]>':
            if top == -1:
                answer = 0
                break
            if char == ')' and stack[top] == '(':
                top -= 1
            elif char == '}' and stack[top] == '{':
                top -= 1
            elif char == ']' and stack[top] == '[':
                top -= 1
            elif char == '>' and stack[top] == '<':
                top -= 1
            else:
                answer = 0
                break

    if top != -1:
        answer = 0

    print(f'#{tc} {answer}')