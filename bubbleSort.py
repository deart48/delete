def bubble_sort(arr):
    n = len(arr)
    counter = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            counter +=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return counter;     

data = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", data)
counter = bubble_sort(data)
print("Отсортированный массив:", data)
print("Количество сравнений:", counter)
