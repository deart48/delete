def quicksort(arr, comparison_count=0):
    if len(arr) <= 1:
        return arr, comparison_count    
    pivot = arr[len(arr) // 2] 
    left = []    
    middle = []  
    right = []   
    for x in arr:
        comparison_count += 1  
        if x < pivot:
            left.append(x)      
        elif x == pivot:
            middle.append(x)    
        else:
            right.append(x)     
    sorted_left, left_comparisons = quicksort(left, comparison_count)
    sorted_right, right_comparisons = quicksort(right, left_comparisons)
    total_comparisons = left_comparisons + right_comparisons
    return sorted_left + middle + sorted_right, total_comparisons



data = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", data)
sorted_data, total_comparisons = quicksort(data)
print("Отсортированный массив:", sorted_data)
print("Общее количество сравнений:", total_comparisons)