# for를 이용한 list 실습

# 조건에 맞는 갯수 
cnt = 0
li = [10, 20, 35, 15]

for i in li:
    if i<=20:
        continue
    print(i)
    cnt += 1
print("건수는", cnt)