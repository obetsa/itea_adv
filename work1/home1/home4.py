'''4. Написать программу, которая запрашивает у пользователя строку чисел, разделённых
пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может
продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь
введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''


result = 0
try:
    while True:
        for i in map(int, input().split()):
            result += i
        print(result)
except ValueError as err:
    print(err)