# Регулярные выражения
# 1. Положительное число меньше 300
# Напишите функцию:
# def is_positive_less_than_300(value):
# Функция должна возвращать True, если строка содержит целое положительное число от 1 до 299.
# Подходят:
# 1
# 15
# 99
# 100
# 299
# Не подходят:
# 0
# 300
# -5
# 3.14
# Abc
import re


# 1. Положительное число меньше 300

def is_positive_less_than_300(value):
    pattern = r"^(?:[1-9]|[1-9][0-9]|[12][0-9]{2})$"
    return bool(re.fullmatch(pattern, value))


print("Task 1:")
print(is_positive_less_than_300("1"))       # True
print(is_positive_less_than_300("15"))      # True
print(is_positive_less_than_300("99"))      # True
print(is_positive_less_than_300("100"))     # True
print(is_positive_less_than_300("299"))     # True
print(is_positive_less_than_300("0"))       # False
print(is_positive_less_than_300("300"))     # False
print(is_positive_less_than_300("-5"))      # False
print(is_positive_less_than_300("3.14"))    # False
print(is_positive_less_than_300("Abc"))     # False
#
#  2. Число от 1 до 255
# Напишите функцию: def is_number_from_1_to_255(value):
# Функция должна проверять целое число от 1 до 255 включительно.
# Подходят:
# 1
# 25
# 100
# 255
# Не подходят:
# 0
# 256
# 25
# -1
# 2.5
# 2. Число от 1 до 255

def is_number_from_1_to_255(value):
    pattern = r"^(?:[1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    return bool(re.fullmatch(pattern, value))


print("\nTask 2:")
print(is_number_from_1_to_255("1"))       # True
print(is_number_from_1_to_255("25"))      # True
print(is_number_from_1_to_255("100"))     # True
print(is_number_from_1_to_255("255"))     # True
print(is_number_from_1_to_255("0"))       # False
print(is_number_from_1_to_255("256"))     # False
print(is_number_from_1_to_255("025"))     # False
print(is_number_from_1_to_255("-1"))      # False
print(is_number_from_1_to_255("2.5"))     # False
#
# 3. Израильский мобильный номер
# Напишите функцию: def is_israel_mobile(phone):
# Допустимы номера:
# 541234567
# 054-1234567
# 92564
# 058-12-34-567
# Не подходят:
# 54-1234567
# 054--12-4567
# 967364
# 97254-123-4567
# 3. Израильский мобильный номер

def is_israel_mobile(phone):
    pattern = r"^(?:05[0-9][0-9]{7}|05[0-9]-[0-9]{7}|\+9725[0-9]-[0-9]{3}-[0-9]{4}|05[0-9]-[0-9]{2}-[0-9]{2}-[0-9]{3})$"
    return bool(re.fullmatch(pattern, phone))

print("\nTask 3:")
print(is_israel_mobile("0541234567"))        # True
print(is_israel_mobile("054-1234567"))        # True
print(is_israel_mobile("+97254-123-4567"))    # True
print(is_israel_mobile("058-12-34-567"))      # True
print(is_israel_mobile("54-1234567"))         # False
print(is_israel_mobile("054--12-4567"))       # False
print(is_israel_mobile("+972054-123-4567"))   # False
print(is_israel_mobile("97254-123-4567"))     # False

#
# 4. Проверка времени Напишите функцию: def is_valid_time(time):
# Формат времени: HH:MM (24 часа).
# Подходят:
# 0:00
# 9:30
# 14:45
# 23:59
# Не подходят:
# 24:00:00
# 0.541666667
# 8:30
# 123:45:00
# Dec-30
# 4. Проверка времени

def is_valid_time(time):
    pattern = r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]$"
    return bool(re.fullmatch(pattern, time))

print("\nTask 4:")
print(is_valid_time("00:00"))    # True
print(is_valid_time("09:30"))    # True
print(is_valid_time("14:45"))    # True
print(is_valid_time("23:59"))    # True
print(is_valid_time("24:00"))    # False
print(is_valid_time("12:60"))    # False
print(is_valid_time("8:30"))     # False
print(is_valid_time("123:45"))   # False
print(is_valid_time("12-30"))    # False
#
# 5. Advance Проверка автомобильного номера Израиля
# Напишите функцию:
# def is_israel_car_number(number):
# Поддержите два формата:
# 12-345-67
# 123-45-678
# Подходят:
# 12-345-67
# 99-999-99
# 123-45-678
# 456-78-901
# Не подходят:
# 12345678
# 12:345:67
# 1-234-56
# 1234-56-78
# 5. Проверка автомобильного номера Израиля

def is_israel_car_number(number):
    pattern = r"^(?:[0-9]{2}-[0-9]{3}-[0-9]{2}|[0-9]{3}-[0-9]{2}-[0-9]{3})$"
    return bool(re.fullmatch(pattern, number))


print("\nTask 5:")
print(is_israel_car_number("12-345-67"))     # True
print(is_israel_car_number("99-999-99"))     # True
print(is_israel_car_number("123-45-678"))    # True
print(is_israel_car_number("456-78-901"))    # True
print(is_israel_car_number("12345678"))      # False
print(is_israel_car_number("12:345:67"))     # False
print(is_israel_car_number("1-234-56"))       # False
print(is_israel_car_number("1234-56-78"))     # False