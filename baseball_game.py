# 숫자야구게임

import random
c1 = int(random.randrange(0,9))
c2 = int(random.randrange(0,9))
c3 = int(random.randrange(0,9))
print(c1, c2, c3)

u1, u2, u3 = map(int,input("숫자를 입력해주세요 : ").split())

s = 0
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

if s==3:
    print("정답입니다.")
    exit()
if s==0 and b==0:
    print("파울입니다.")
    exit()

print("{} 스트라이크 {} 입니다.".format(s, b))
