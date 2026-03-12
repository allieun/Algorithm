n = int(input())
prize_list = []
for _ in range(n):
    solve, penalty = map(int, input().split())
    prize_list.append([-solve, penalty])

prize_list.sort()

if n > 5:
    target_chicken = prize_list[4][0]
    count = 0
    for i in range(5, n):
        if prize_list[i][0] == target_chicken:
            count += 1
    print(count)
else:
    print(0)