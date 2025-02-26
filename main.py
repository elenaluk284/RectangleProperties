# Функция для расчета площади и периметра прямоугольника
def calculate_rectangle_properties():
    # Ввод длины и ширины
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))

    # Вычисление площади
    area = length * width

    # Вычисление периметра
    perimeter = 2 * (length + width)

    # Вывод результатов
    print(f"Площадь прямоугольника: {area}")
    print(f"Периметр прямоугольника: {perimeter}")


# Вызов функции
calculate_rectangle_properties()
