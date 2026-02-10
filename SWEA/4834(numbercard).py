'''
목적: 가장 많은 카드에 적힌 숫자와 그 카드가 몇 장인지 출력하는 프로그램 만들기 (최다 카드가 여러 종류일 때는 더 큰 수 출력)
-> 카운팅 정렬을 쓰는 것이 좋을 듯 하다
1. 일단 카드 장수 n과 길이 n 만큼의 리스트를 받는다
2. 카운팅할 리스트 따로 받는다
3. 카운팅 정렬한 리스트에서 가장 큰 값과 그 값의 인덱스를 반환한다.
4. 장수가 같을 때는 가장 큰 숫자를 가진 카드와 그 카드의 장수 차례대로 출력
'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    cards = list(map(int, input()))

    count_list = [0] * 10                                # 카드의 범위가 0부터 9까지이기 때문

    for card in cards:
        count_list[card] += 1                            # 카운팅 정렬을 활용해 빈 리스트에 인덱스에 해당하는 값 나올 때 마다 +1

    max_card = max(count_list)                           # 카운팅 리스트에서 가장 큰 값 = 가장 많은 장수를 가진 카드

    for i in range(9, -1, -1):                           # 리스트를 역으로 순회하며 max_card가 인데스 i의 값과 같다면 그 인덱스 값을 반환
        if count_list[i] == max_card:
            max_idx = i                                  # 만약 최대 장수의 카드의 종류가 여러개 있다면 역순으로 리스트를 순회하기 떄문에 더 큰 수의 카드가 출력됨
            break    

    print(f'#{tc} {max_idx} {max_card}')