def swap_string_array(input_array):
    left = 0 
    right = len(input_array) - 1 
  
    while left < right:
        temp = input_array[left]
        input_array[left] = input_array[right]
        input_array[right] = temp
        left += 1 
        right -= 1 
        #print(input_array)
        
    return input_array

def string_to_array(input_string):
    input_array = list(input_string)
    return input_array

def array_to_string(input_array):
    return "".join(input_array)

def validation(input_array):
    return len(input_array) == 0
    
def print_answer(input_string):
    input_array = string_to_array(input_string)
    if validation(input_array):
        print("It is an empty string.")
    else:
        print("The reverse string is : ", array_to_string(swap_string_array(input_array)))

input_string = "HELLO"
print_answer(input_string)
