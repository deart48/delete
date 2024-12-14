def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0 
    
    while low <= high:
        mid = (low + high) // 2 
        comparisons += 1 
        
        if arr[mid] == target:
            return mid, comparisons 
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  
    
    return -1, comparisons  


sorted_array = [1, 2, 5, 5, 6, 9]
target_value = 5
target_value1 = 9
target_value2 = 1
target_value3 = 10

index, total_comparisons = binary_search(sorted_array, target_value3) #, target_value1, target_value2, target_value3)

if index != -1:
    print(f"Элемент найден на индексе: {index}")
else:
    print("Элемент не найден")
print(f"Общее количество сравнений: {total_comparisons}")

#лучший случай o(log(n))