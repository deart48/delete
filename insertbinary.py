def binary_search_position(arr, target, end):
    low, high = 0, end - 1
    comparisons = 0  

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1  
        
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low, comparisons  

def insertion_sort_with_binary_search(arr):
    total_comparisons = 0  

    for i in range(1, len(arr)):
        target = arr[i]
        position, comparisons = binary_search_position(arr, target, i)
        total_comparisons += comparisons  
        total_comparisons += 1
        
        arr[position + 1:i + 1] = arr[position:i] 
        arr[position] = target  

    return arr, total_comparisons  


arr = [5, 2, 9, 1, 5, 6]
arr2 = [7, 6, 5, 4, 3] 
arr3 = [1, 2, 5, 8, 12]
# arr = [1,2,5,5,6,6,7,9]
#arr = [9,8,7,6,5,4,3,2]

sorted_arr, total_comparisons = insertion_sort_with_binary_search(arr3)#,arr2,arr3)
print("Отсортированный массив:", sorted_arr)
print("Общее количество сравнений:", total_comparisons)
#лучший o(n*log(n))
#худший o(n^2)
#средний o(n^2)