'''
두 집합 A와 B의 대칭 차집합의 개수를 계산하는 코드 작성

1. 집합 A의 원소 개수와 집합 B의 원소 개수가 빈칸을 사이에 두고 주어짐
2. 집합 A의 모든 원소가 주어짐
3. 집합 B의 모든 원소가 주어짐
4. 연산 속도 떄문에 list로 만들지 말고 set으로 만들어 처리 속도 향상
'''

a, b = map(int, input().split())
a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))

count = 0

for a in a_list:
    if a not in b_list:
        count += 1

for b in b_list:
    if b not in a_list:
        count += 1

print(count)
