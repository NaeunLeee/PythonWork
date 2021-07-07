def bmi(h, w):
    b = w/(h/100 * h/100)
    grade = ""
    if b<18.5:
        grade = "저체중"
    elif 18.5<=b<23:          
        grade = "정상"
    elif 23<=b<25:
        grade = "과체중"
    elif 25<=b<30:
        grade = "비만"
    else:
        grade = "고도비만"
    return grade

result = bmi(160, 60)
print(result)