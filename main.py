def bubble_sort(arr):
    """Сортирует список arr по возрастанию с помощью алгоритма пузырька."""
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации: если за проход не было обменов — список отсортирован
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    try:
        # Запрашиваем количество чисел
        n = int(input("Введите количество чисел: "))
        if n <= 0:
            print("Количество должно быть положительным числом.")
            return

        numbers = []
        print(f"Введите {n} чисел (целых или дробных):")
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Число {i + 1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")

        # Сортируем
        sorted_numbers = bubble_sort(numbers)

        # Выводим результат
        print("\nОтсортированный список по возрастанию:")
        # Если число целое — выводим как целое, иначе как дробное
        formatted = [int(x) if x.is_integer() else x for x in sorted_numbers]
        print(formatted)

    except ValueError:
        print("Ошибка: введите корректное целое число для количества.")

if __name__ == "__main__":
    main()