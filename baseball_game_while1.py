# 숫자야구게임_맞출 때까지 반복

import random
c1 = int(random.randrange(0,9))
c2 = int(random.randrange(0,9))
c3 = int(random.randrange(0,9))
print(c1, c2, c3)

s = 0
while s < 3:
    u1, u2, u3 = map(int,input("숫자를 입력해주세요 : ").split())
    s = 0       # s를 다시 0으로 초기화
    b = 0
    if c1==u1:
        s += 1
    elif c1==u2 or c1==u3:
        b += 1
    if c2==u2:
        s += 1
    elif c2==u1 or c2==u3:
        b += 1
    if c3==u3:
        s += 1
    elif c3==u1 or c3==u2:
        b += 1
    if s==0 and b==0:
        print("파울입니다.")
    print("{} 스트라이크 {} 볼 입니다.".format(s, b))
print("정답입니다!!")