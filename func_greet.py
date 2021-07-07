# 인사하는 함수
# 함수 선언

def greet_times(name, cnt):
    print(name)
    for i in range(cnt):
        print("안녕하세요")
    # return이 생략되어 있음

greet_times("이나은", 2)      # 함수 실행 (=함수 호출)
greet_times("김유신", 3)

