def max_sub_array_sum(input_array, sub_array_length):
    window_sum = sum(input_array[0:sub_array_length])
    max_sum = window_sum
    
    if len(input_array) < sub_array_length:
        return None
        
    for i in range(sub_array_length, len(input_array)):
        window_sum += input_array[i]
        window_sum -= input_array[i - sub_array_length]
        max_sum = max(window_sum, max_sum)
    return max_sum
    
array1 = [1,-2,3,-4,5,6]
sub_array_length = 3

print(max_sub_array_sum(array1, sub_array_length))
