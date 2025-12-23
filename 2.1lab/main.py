if __name__ == "__main__":
    pass


my_dict = {'b': 1, 'a': 2, 'c': 3}
print(f"Исходный словарь: {my_dict}")

sorted_dict = dict(sorted(my_dict.items()))
print(f"Отсортированный словарь: {sorted_dict}")

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"Исходный словарь: {my_dict}")

print("\nКлючи, значения и элементы:")
for key, value in my_dict.items():
    print(f"key: {key}, value: {value}, item: ({key}, {value})")

my_dict = {'a': '1', 'b': '2', 'c': '3.0', 'd': '4.5', 'e': 'abc'}
print(f"Исходный словарь: {my_dict}")

converted_dict = {}
for key, value in my_dict.items():
    if value.isdigit():
        converted_dict[key] = int(value)
    else:
        try:
            converted_dict[key] = float(value)
        except ValueError:
            converted_dict[key] = value

print(f"Преобразованный словарь: {converted_dict}")
