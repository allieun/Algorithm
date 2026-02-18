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

'''
def price(month, current_sum):
    global min_price

    if current_sum >= min_price:
        return
    if month >= 12:
        if current_sum < min_price:
            min_price = current_sum
        return
    
    price(month+1, current_sum + (month_list[month] * price_list[0]))
    price(month+1, current_sum + price_list[1])
    price(month+3, current_sum + price_list[2])




t = int(input())

for tc in range(1, t+1):
    price_list = list(map(int, input().split()))
    month_list = list(map(int, input().split()))

    min_price = price_list[3]

    price(0, 0)

    print(f'#{tc} {min_price}')