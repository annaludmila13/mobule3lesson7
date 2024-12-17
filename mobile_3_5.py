def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    first = int(str_number[0])  # Берем первую цифру и преобразуем в int

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))  # Умножаем первую цифру на результат рекурсии
    else:
        return first  # Если осталась одна цифра, просто возвращаем её

result = get_multiplied_digits(40203)
print(result)