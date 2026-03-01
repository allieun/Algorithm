'''
숫자카드 N개를 가지고 있는 상황에서 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 가지고 있는지의 여부를 확인하는 코드

첫째 줄 : 가지고 있는 숫자 카드의 개수
둘째 줄 : 숫자카드에 적혀있는 정수
셋재 줄 : 정수 M
넷째 줄 : 가지고 있는 숫자카드인지 아닌지 구분해야 할 M개의 정수

1. 카운트 전용 0만 담긴 리스트를 생성한 후 길이는 m으로 설정
2. 구분해야 할 숫자가 카드 목록에 있다면 카운트 전용 리스트 인덱스에 1로 변경
3. 카운트 리스트 언패킹 한 후 출력
'''

n = int(input())
card_num = set(map(int, input().split()))                  # set를 쓰지 않는다면 시간초과 에러 메시지가 뜸
m = int(input())
find_num = list(map(int, input().split()))

count_list = [0] * m                                       # m의 길이만큼 0으로 차있는 리스트 넣기

for i in range(m):
    if find_num[i] in card_num:
        count_list[i] = 1
    else:                                                 # 이 부분은 생략해도 됨(이미 리스트의 해당 인덱스 값은 0이기 때문)
        count_list[i] = 0

print(*count_list)