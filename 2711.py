# 오타맨 고창영 (2711)

tst = int(input("테스트 횟수 입력 : "))

for i in range(tst):
    n, st = input("오타 위치와 문자열 입력 : ").split()
    n = int(n)
    print(st[:n-1], st[n:], sep='')

# for i in range(tst):
#     n, st = input("오타 위치와 문자열 입력 : ").split()
#     n = int(n)
#     li = list(st)
#     del li[n-1]
#     for i in range(len(li)):
#         print(li[i], end='')
