# def func():
#     a = 1
#     b = 2
#     return a + b
#
# def sum(a):
#     def add(b):
#         return a + b
#     return add
#
# num1 = func()
# num2 = sum(2)
#
# print(type(num1))
# print(type(num2))

# def func():
#     a = 1
#     b = 2
#     return a + b
#
# def sum(a):
#     def add(b):
#         return a + b
#     return add
#
# # add 函数名称或函数的引用
# # add() 函数的调用
# num1 = func()
# num2 = sum(2)
# print(num2(4))

# def counter():
#     cnt = [0]
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#     return add_one
#
# num1 = counter()
#
# print(num1())
# print(num1())
# print(num1())
# print(num1())

def counter(FIRST=0):
    cnt = [FIRST]

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num5 = counter(5)
num10 = counter(10)

print(num5())
print(num5())
print(num5())
print(num10())
print(num10())
