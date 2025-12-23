if __name__ == "__main__":
    pass





python
print("1. Проверка степени двойки (исключения)")
print("2. Проверка палиндрома (исключения)")
print("3. Проверка степени двойки (assert)")

choice = input("Выберите задачу (1-3): ")

if choice == '1':
    num = int(input("Введите число: "))
    if num <= 0:
        raise ValueError("Число должно быть положительным")
    if (num & (num - 1)) == 0:
        print("Число является степенью двойки")
    else:
        raise Exception("Число не является степенью двойки")

elif choice == '2':
    text = input("Введите строку: ")
    cleaned_text = ''.join(text.lower().split())
    if cleaned_text == cleaned_text[::-1]:
        print("Строка является палиндромом")
    else:
        raise Exception("Строка не является палиндромом")

elif choice == '3':
    num = int(input("Введите число: "))
    assert num > 0, "Число должно быть положительным"
    assert (num & (num - 1)) == 0, "Число не является степенью двойки"
    print("Число является степенью двойки")

else:
    print("Неверный выбор")
