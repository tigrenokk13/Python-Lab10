# Функція для відкриття файлу
def open_file(filename):
    try:
        file = open(filename, "w")
        print("Файл успішно відкрито!")
        return file
    except Exception as e:
        print(f"Не вдалося відкрити файл! Помилка: {e}")
        return None

# Функція для запису рядків у файл
def write_to_file(file):
    file = open_file(filename)
    if file is not None:
        try:

            # (Стешенко Станіслав КН-31.1)
            file.write("Стешенко Станіслав КН-31.1\n")
            file.write("Питання 1: Як вивести текст на екран у Python?\n")
            
            # Закриття файлу після запису
            file.close()
            print("Дані успішно записані у файл.")
            print("Файл успішно закрито!")
        except Exception as e:
            print(f"Виникла помилка під час запису у файл: {e}")
    else:
        print("Файл не було відкрито, запис неможливий.")

# (Стешенко Станіслав КН-31.1)
# Виклик функцій
filename = "Lab-10.txt"
write_to_file(filename)
