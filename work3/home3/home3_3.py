"""3. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
Решение покрыть тестами (опционально)."""

from pathlib import Path
path = Path(__file__).resolve().parent
file_path = path / "new_file.txt"
file_path1 = path / "new_file1.txt"



with open(file_path, "w") as f:
    f.write('One - 1\nTwo - 2\nThree - 3\nFour - 4')


with open(file_path, "r") as f:
    f.seek(0)
    text = f.read()
    text = text.replace("One", "Один")
    print(f.readlines())
    with open(file_path1, "w") as f:
        f.write(text)
