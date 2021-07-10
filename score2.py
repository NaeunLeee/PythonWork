# 학생 4명의 국어, 영어, 수학 성적을 저장
score = [[90, 70, 30], [40, 50, 50], [100, 90, 80], [80, 80, 80]]

# 영어성적의 합을 계산 (range, index로)
eng_total = 0
for i in range(len(score)):
    eng_total += score[i][1]
print(eng_total)
# 영어성적의 합을 계산 (element로)
eng_total = 0
for el in score:
    eng_total += el[1]
print(eng_total)



