'''3. Реализовать функцию, которая принимает три позиционных аргумента и возвращает
сумму наибольших двух из них.'''

a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))

if a < b:
    min = a
else:
    min = b
if c < min:
    min = c
sum = a + b + c - min

print("Summa: ", sum)