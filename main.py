def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if reverse:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    print("Введите числа через пробел:")
    numbers = list(map(int, input().split()))
    
    print("Выберите направление сортировки:")
    print("1 - по возрастанию")
    print("2 - по убыванию")
    
    choice = input("Ваш выбор (1 или 2): ")
    
    if choice == "2":
        sorted_numbers = bubble_sort(numbers.copy(), reverse=True)
        print("Отсортированные числа по убыванию:")
    else:
        sorted_numbers = bubble_sort(numbers.copy())
        print("Отсортированные числа по возрастанию:")
    
    print(' '.join(map(str, sorted_numbers)))

if __name__ == "__main__":
    main()
