def my_sum(li):
    total = 0
    for i in li:
        total += i
    return total

print(my_sum([1, 2, 3]))
print(my_sum([10, 2, 35, 61]))

def my_cal(a, b):
    cal = a*b+b
    return cal

print(my_cal(1, 2))
print(my_cal(4,5))