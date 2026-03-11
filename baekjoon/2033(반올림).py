'''
정수 N이 10보다 크면 1의 자리 반올림 진행, 이 결과가 100보다 크면 10의 자리 반올림 진행 -> 더 이상 반올림 진행할 수 없을 때 까지 반올림 진행

풀이 로직 : 재귀를 사용한 하나 전 자리수의 확인 및 반올림 진행

'''

n = int(input())

compare = 10

while n > compare:
    if n % compare >= 5 * (compare // 10):
        n = (n // compare + 1) * compare
    else:
        n = (n // compare) * compare

    compare *= 10

print(n)