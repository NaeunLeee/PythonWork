# 10~39 입력한 값을 나이대별로 #로 카운트

li = [15, 11, 24, 39, 23]
cnt = [0, 0, 0, 0]
for x in li:
    cnt[x//10] += 1
for y in cnt:
    print('#'*y)


