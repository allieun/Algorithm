'''
n개의 문자열로 이루어진 집합 s에서 m 개의 문자열이 입력되었을 때 s에 포함되어있는 요소가 총 몇 개인지 구하기.
여기서도 처음에 두개 다 리스트로 받았다가 시간초과 및 런타임 오류 에러가 떴기 떄문에 입력은 set로 받기

'''

n, m = map(int, input().split())

s = set(input() for _ in range(n))

count = 0

for _ in range(m):
    check = input().strip()
    if check in s:
        count += 1

print(count)