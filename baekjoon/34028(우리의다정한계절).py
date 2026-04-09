'''
12월 1일 -- 2월 29일: 겨울
3월 1일 -- 5월 31일: 봄
6월 1일 -- 8월 31일: 여름
9월 1일 -- 11월 30일: 가을

여자친구 데뷔일 :  2015년 1월 16일
여자친구의 데뷔일로부터 입력한 날짜까지 몇 번의 계절을 함께했는지 구하기
'''
import sys
input = sys.stdin.readline

year, month, day = map(int, input().split())

# 여자친구의 데뷔일 1월 16일은 '겨울'에 속함
d_year, d_month, d_day = 2015, 1, 16

def find_season(y, m, d):

    # 12월을 '작년'으로 취급하면 (12, 1, 2)가 하나의 연도 안에서 0, 1, 2월이 됨
    if m == 12:
        adjusted_year = y
    else:
        adjusted_year = y - 1
        
    # 계절 번호: 0:겨울(12-2), 1:봄(3-5), 2:여름(6-8), 3:가을(9-11)
    if m in [12, 1, 2]:
        season_num = 0
    elif m in [3, 4, 5]:
        season_num = 1
    elif m in [6, 7, 8]:
        season_num = 2
    else: # 9, 10, 11
        season_num = 3
        
    # '연도 * 4 + 계절번호'를 하면 2015년 겨울부터의 절대적인 순서가 나옴
    return adjusted_year * 4 + season_num

# 3. 시작점과 끝점의 계절 인덱스 계산
start_idx = find_season(d_year, d_month, d_day)
end_idx = find_season(year, month, day)

# 4. '일부만 포함해도 한 번'이므로 두 인덱스의 차이 + 1
# (예: 같은 계절이면 0 + 1 = 1번)
result = end_idx - start_idx + 1

print(result)