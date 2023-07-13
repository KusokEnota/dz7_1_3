"""Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере"""

from pathlib import Path


# модуль для работы с путями файловой системы и проходит по всем файлам в текущем рабочем каталоге

def rename_file(new_name, source_extension, new_extension):
    """""
    Групповое переименование файлов с добавлением порядкового номера в текущем рабочем каталоге.

    :param new_name: Желаемое конечное имя файлов.
    :param source_extension: Расширение исходных файлов.
    :param new_extension: Расширение конечных файлов.
    """""
    directory = Path.cwd()
    files = list(directory.glob(f"*{source_extension}"))
    # print(files)
    renamed_count = 0
    for index, file in enumerate(files, start=1):
        new_file_name = f"{new_name}_{index}.{new_extension}"
        file.rename(directory / new_file_name)
        renamed_count += 1

        print(f"Файл переименован: {file.name} -> {new_file_name}")

    if renamed_count == 0:
        print("Нет файлов с указанным расширением.")
        return

    print(f"Переименовано файлов: {renamed_count}")


if __name__ == '__main__':
    rename_file("new_name", "txt", "md")
