def shell_sort(arr):
    n = len(arr)
    counter = 0  
    gap = n // 2  
   
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                counter += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return counter;


data = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", data)
counter = shell_sort(data)
print("Отсортированный массив:", data)
print("Количество сравнений:", counter)
