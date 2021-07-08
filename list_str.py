# 글자수만큼 반복
# 글자가 1이면 카운트 증가

s = '1011000011'
cnt = 0
for i in s:
    if i == '1':
        cnt += 1
print("1은 {}개입니다.".format(cnt))
