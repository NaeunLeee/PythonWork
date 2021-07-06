# 숫자 맞추기 게임

# 1. 임의의 수 생성
# 2. 숫자 입력
# 3. 입력값이 크다면 크다라고 출력
#             작다면 작다라고 출력
#             맞으면 맞다라고 출력하고 프로그램 종료 exit() 함수 이용
# 4. 3번을 4번 반복
# 5. "게임오버"라고 출력

import random
com = int(random.randrange(1,10))

num = int(input("숫자를 입력해주세요 : "))
if num>com:
    print("큽니다.")
elif num<com:
    print("작습니다.")
elif num==com:
    print("맞습니다.")
    exit()

num = int(input("숫자를 입력해주세요 : "))
if num>com:
    print("큽니다.")
elif num<com:
    print("작습니다.")
elif num==com:
    print("맞습니다.")
    exit()

num = int(input("숫자를 입력해주세요 : "))
if num>com:
    print("큽니다.")
elif num<com:
    print("작습니다.")
elif num==com:
    print("맞습니다.")
    exit()

num = int(input("숫자를 입력해주세요 : "))
if num>com:
    print("큽니다.")
elif num<com:
    print("작습니다.")
elif num==com:
    print("가까스로 맞췄습니다ㅋㅋ")
    exit()

print("Game Over")


