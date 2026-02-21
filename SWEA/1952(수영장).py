'''
판매하는 이용권 종류 4가지 (일일권 / 1개월권 / 3개월권 / 1년 권)
이용권 별 금액은 그때그때 새로 주어진다.
각 달 별 이용 일수가 주어질 때, 어떻게 이용권을 구입해야 가장 적은 금액을 소비할 수 있을지 구하자.

포인트 : 일단 1년권이 가장 비싼 값이라고 가정하고 진행한다
1. 테스트 케이스 숫자와 4개의 이용권 가격 입력 받음
2. 다음 줄에 월별 이용 일수 입력받음(리스트)
3. 테스트 케이스 밖에 3가지의 경우의 수를 고려하는 함수 지정
    (3가지인 이유는 1일권, 1개월권, 3개월권의 경우의 수를 1년권 금액과 비교해 더 적은 금액을 정답으로 하면 되기 때문)
4. 금액을 비교하는 함수를 설정
5. 함수에서 고려할 요소
    1) 전부 1일권으로 구매했을 때
    2) 전부 1개월 권으로 구매했을 때
    3) 전부 3개월 권으로 구매 했을 때
6. 이 함수에서는 global로 min_price를 불러와서 각각의 케이스와 비교 후 최소비용을 확정

'''
def price(month, current_sum):
    global min_price                      # tc에서 min_price로 지정한 price_list[3] 불러오기  = 1년권 금액

    if current_sum >= min_price:          # 지금 더한 가격이 min_price 값 보다 크면 이 조건문 종료
        return
    if month >= 12:                       # 월의 수가 12를 지난다면?
        if current_sum < min_price:       # 이 경우에서 min_price보다 현재 값이 작다면 그것을 min_price로 변경
            min_price = current_sum
        return                            # 조건문 종료
    
    price(month+1, current_sum + (month_list[month] * price_list[0]))       # 1일권으로만 구매했을 때
    price(month+1, current_sum + price_list[1])                             # 1개월권으로만 구매했을 때
    price(month+3, current_sum + price_list[2])                             # 3개월 권으로만 구매했을 때




t = int(input())

for tc in range(1, t+1):
    price_list = list(map(int, input().split()))          # 이용권 가격 4가지 입력 받기
    month_list = list(map(int, input().split()))          # 월별 이용 일수 입력받기

    min_price = price_list[3]                             # 최저금액을 1년권 금액으로 임시 지정(이용권 가격들 중 가장 비싸기 때문)

    price(0, 0)                                           # 현재 금액 0원, 1월 1일 부터 시작

    print(f'#{tc} {min_price}')