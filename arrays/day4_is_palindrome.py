# after editing the String

def is_palindrome(input_array):
    left = 0
    right = len(input_array) - 1 
    
    while left < right:
        if input_array[left] != input_array[right]:
            return False
        left += 1 
        right -= 1 
    return True

def convert_string(input_string):
    input_array = list(input_string)
    usable_array = []
    for element in input_array:
        if element.isalnum():
            usable_array.append(element.lower())
    return usable_array
    
def is_Empty(input_array):
    return len(input_array) == 0
    
def print_answer(input_string):
    #convert the string to usable input
    usable_array = convert_string(input_string)
    
    #check for empty String
    if is_Empty(usable_array):
        print("The string is Empty")
    else:
        #check for palindrome
        if is_palindrome(usable_array):
            print(input_string, ": Is a Palindrome")
        else:
            print(input_string, ": Is not a Palindrome")
    
String1 = "A man a plan a canal Panama"
print_answer(String1)
