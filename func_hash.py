# def func_tri(num):
#     for i in range(1, num+1):
#         print('#'*i)
# func_tri(5)
# print()
# func_tri(3)

def func_tree(h):
    for i in range(1, h+1):
        print(' '*(h-i), '#'*(i*2-1))
func_tree(5)