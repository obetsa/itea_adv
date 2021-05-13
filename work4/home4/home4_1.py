"""1. Реализовать функцию, которая на вход принимает целое положительное число n и возвращает при вызове
 объект-генератор, который по запросу будет возвращать значение факториала всех чисел от 0 до n.
 5! = 1 * 2 * 3 * 4 * 5 
"""

try:
    n = int(input("Enter number: "))
except ValueError:
    print("Not a number")
except Exception:
    print("what is this??)")


def number():
    pass

def fibonacchi(n):
    a = 1
    b = 1
    i = 0
    while i < n - 2:
        summa = a + b
        a = b
        b = summa
        i = i + 1
 
    print("Значення: ", b)


fibonacchi(n)

