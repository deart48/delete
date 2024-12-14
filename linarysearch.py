def linear_search(arr, target):
    comparisons = 0 
    
    for index, value in enumerate(arr):
        comparisons += 1 
        if value == target:
            return index, comparisons  

    return -1, comparisons 


array = [3, 5, 2, 4, 9, 1, 6]
target_value = 4
target_value1 = 6
target_value2 = 3
target_value3 = 100

index, total_comparisons = linear_search(array, target_value2) #target_value) #, target_value1, target_value2, 

if index != -1:
    print(f"Элемент найден на индексе: {index}")
else:
    print("Элемент не найден")
print(f"Общее количество сравнений: {total_comparisons}")

#лучший случай o(n)