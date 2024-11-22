def generate_password(n):
    result = ""

    # Генерируем пары (a, b)
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            s = a + b  # Сумма пары

            # Проверяем кратность
            if n % s == 0:
                result += str(a) + str(b)

    return result


# Пример использования
n = 11  # Можно заменить на любое число от 3 до 20
password = generate_password(n)
print("Сгенерированный пароль:", password)
