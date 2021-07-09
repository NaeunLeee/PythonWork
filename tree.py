# 백준 Tree 만들기

height = int(input("Tree의 높이를 입력하세요 (1~30) : "))
# for i in range(0, height):
#     print(' '*(height-i), "*"*(i*2+1))
# for i in range(0, 3):
#     print(' '*(height-1), "***")
for x in range(1, height+1):
    print(' '*(height-x), "*"*(x*2-1))
for y in range(1, 4):
    print(' '*(height-2), "***")