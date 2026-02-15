'''
첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들어서 새로운 문자열 P를 출력

핵심은 r을 문자열(string)의 형태로 받았기 때문에 이걸 정수형으로 변환하는 과정이 필요하다는 점
'''

n = int(input())

for _ in range(n):
    r, s = input().split()
    r = int(r)
    word = []
    for w in s:
        word.append(w*r)

    print(*word, sep='')