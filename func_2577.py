# 숫자의 개수 (2577)

def f_2577(a, b, c):
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in str(a*b*c):
        cnt[int(i)] += 1
    return cnt

li = f_2577(150, 266, 427)
for i in li:
    print(i)
