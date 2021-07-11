# 별 찍기 (2523)

n = int(input("N 입력 (1~100) : "))

for i in range(1, n+1):
    print('*'*i)
for i in range(n-1, 0, -1):
    print('*'*i)

