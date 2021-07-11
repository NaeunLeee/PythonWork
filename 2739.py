# 구구단 (2739)

n = int(input("숫자 입력 : "))

for i in range(9):
    print("{} * {} = {}".format(n, (i+1), n*(i+1)))
