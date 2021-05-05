'''1. Написать декоратор, который будет печатать на экран время работы функции.'''

# 1

import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped

@time_of_function
def func(first, second):
    return bin(int(first, 2) + int(second, 2))


print(func("11111", "0000000"))




# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         execution_time = time.time() - start
#         print(f"\nExecution time {func.__name__} {execution_time} seconds")

#         return result

#     return wrapper


# @time_decorator
# def func():
#     a = 1
#     b = 1
#     n = input("Номер елемента: ")
#     n = int(n)
#     i = 0
#     while i < n - 2:
#         sum = a + b
#         a = b
#         b = sum
#         i = i + 1
 
#     print("Значення: ", b)

    
# print(func("111", "0000"))