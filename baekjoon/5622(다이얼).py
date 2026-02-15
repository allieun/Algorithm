'''
다이얼이 주어지고, 각 숫자에 맞는 알파벳 문자가 할당됨
1은 할당 x, 2부터 9까지 각각 3-4개씩 (2-ABC, 3-DEF, ..., 7-PQRS, ..., 9-WXYZ)

목표: 다이얼을 돌리는 최소 시간 구하기 -> 딕셔너리로 한 번 풀어볼까?

1. 각 다이얼의 위치에 맞체 딕셔너리 key와 value 값 구성
2. 단어 입력 받음
3. key 값: 알파벳, value 값(숫자당 배치된 알파벳 3-4개) : 다이얼 숫자
4. 입력받은 단어의 딕셔너리 내부 키값을 찾아 매치
5. 키값에 1을 더해 전체 시간에 더함
'''

word_dict = {
    'ABC' : 2,
    'DEF' : 3,
    'GHI' : 4,
    'JKL' : 5,
    'MNO' : 6,
    'PQRS' : 7,
    'TUV' : 8,
    'WXYZ' : 9
}

word = input()

time = 0

for char in word:
    for key in word_dict:
        if char in key:
            time += word_dict[key] + 1

print(time)