# 삼각형 출력

'''
#####
#####
#####
#####
#####
'''
# range(e) -> 0~(e-1) 1씩 증가
# range(s,e) -> s~(e-1) 1씩 증가
# range(s,e,step) -> s~(e-1) step씩 증가

# for i in range(5):
#     print("#"*i)
# for i in range(1,9):
#     print("#"*i)
# for i in range(9,0,-2):         # 역삼각형
#     print("#"*i)
# for i in range(1,10):
#     print(' '*(10-i), '#'*i)
# for i in range(1,10,2):
#     print(' '*(10-i), '#'*i)
# for i in range(1,10,2):
#     print(' '*(10-i), end='')
#     print('#'*(10-i))
# cnt = 10
# for i in range(1, cnt):
#     print(" "*(cnt-i), end = ' ')
#     print("#"*(cnt-i))
cnt = int(input())
for i in range(0,cnt):
    print(" "*(cnt-i), "#"*(i*2+1))
# for i in range(0,cnt):
#     print(" "*(cnt-1), "#"*(i))

