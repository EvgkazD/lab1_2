def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))

    sorted_numbers = bubble_sort_ascending(numbers.copy())

    print("Отсортированные числа по возрастанию:")
    print(' '.join(map(str, sorted_numbers)))


if __name__ == "__main__":
    main()