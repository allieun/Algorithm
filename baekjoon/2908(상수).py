
'''
숫자 A와 B를 받는다. (두 숫자에는 0이 포함되지 않음)
숫자를 받으면 자리수를 뒤집는다 (123은 321로 변경)
뒤집힌 두 숫자 중 더 큰 숫자를 출력한다
'''


a, b = input().split()

a = a[::-1]                       # int 형태는 뒤집기가 안되기 떄문에 int(input())을 사용하면 안된다
b = b[::-1]

if a > b:
    answer = a
else:
    answer = b

print(answer)