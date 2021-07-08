li = [10, 20, 126, 4, 55, 60, 85, 15, 47, 96]
# 최댓값
# 최댓값 변수에 리스트의 첫번째 값을 저장
# 리스트의 값과 최댓값 변수와 비교해서 리스트 값이 크면 최댓값변수에 저장

max_num = li[0]
min_num = li[0]

for i in li:
    if i < max_num:
        continue
    max_num = i
    
print("최댓값은", max_num)

for i in li:
    if i > min_num:
        continue
    min_num = i
    
print("최솟값은", min_num)

