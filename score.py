# 세 반의 영어 성적

eng = [[90, 70, 30], [100, 50], [60, 50, 50, 70]]

# 전체합계
total = 0
for i in range(len(eng)):
    for j in range(len(eng[i])):
        total += eng[i][j]
print(total)
print("===============")
total = 0
for ban_sc in eng:
    for eng_sc in ban_sc:
        total += eng_sc
print(total)
print("===============")

# 각반별 합계
for i in range(len(eng)):
    s = sum(eng[i])
    print("{}반 : {}점".format(i+1, s))


