'''3. Реализовать функцию, которая принимает три позиционных аргумента и возвращает
сумму наибольших двух из них.'''

# Fixed(hw1 branch)

a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))


def summax(a, b, c):
    if a < b:
        minimal = a
    else:
        minimal = b
    if c < minimal:
        minimal = c
    res = a + b + c - minimal

    print("Summa: ", res)

summax(a, b, c)