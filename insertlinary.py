def linear_search_position(arr, target, end):
    comparisons = 0
    for i in range(end - 1, -1, -1):
        comparisons += 1  
        if arr[i] <= target:
            return i + 1, comparisons  
    return 0, comparisons

def insertion_sort_with_linear_search(arr):
    total_comparisons = 0  

    for i in range(1, len(arr)):
        target = arr[i]
        position, comparisons = linear_search_position(arr, target, i)
        total_comparisons += comparisons  
        # total_comparisons +=1
        
        
        arr[position + 1:i + 1] = arr[position:i]  
        arr[position] = target  

    return arr, total_comparisons  


array = [5, 3, 8, 6, 2]
array2 = [7,6,5,4,3] 
array3 = [1,2,5,8,12]
sorted_array, total_comparisons = insertion_sort_with_linear_search(array3)#,array2, array3)

print(f"Отсортированный массив: {sorted_array}")
print(f"Общее количество сравнений: {total_comparisons}")

#лучший случай o(n)
#средний и худший случай o(n^2)