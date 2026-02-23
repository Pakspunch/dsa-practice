"""Kadane's Algo for max sum sub array
compare current_max + element to element, if less restarts
If carrying forward the previous sum makes things worse than starting fresh, reset the subarray start."""

def return_max_subarray_sum(input_array):
    current_max = input_array[0]
    max_sum = current_max
    
    for element in input_array[1:]:
        current_max = max(element, current_max + element)
        max_sum = max(max_sum, current_max)
        #print(element, current_max, max_sum)

    return max_sum

def return_max_subarray(input_array):
    current_max = input_array[0]
    max_sum = current_max

    temp_start = 0 
    best_start = 0 
    best_end = 0 
    
    for i in range(1, len(input_array)):
        if input_array[i] > current_max + input_array[i]:
            current_max = input_array[i]
            temp_start = i 
        else:
            current_max += input_array[i]
            
        if current_max > max_sum:
            max_sum - current_max
            best_start = temp_start
            best_end = i 
    
    return input_array[best_start: best_end+1]

listA = [-1,2,5,-10,0,8,7]
print("Maximum sum of sub array :", return_max_subarray_sum(listA))
print("The sub array is :", return_max_subarray(listA))
