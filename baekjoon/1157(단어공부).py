word = input().upper()

def check(word):
    words = list(set(word))

    check_list = []
    for i in words:
        count = word.count(i)
        check_list.append(count)
    
    if check_list.count(max(check_list)) > 1:
        return '?'
    else:
        answer = words[check_list.index(max(check_list))]
        return answer
result = check(word)
print(result)
