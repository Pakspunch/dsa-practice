def character_count(input_array):
    char_freq = {}
    count = 0
    
    for i in range(len(input_array)):
        current_char = input_array[i]
        
        if current_char in char_freq:
            char_freq[current_char] += 1 
        else:
            char_freq[current_char] = 1
    return char_freq

def is_palindrome(char_freq):
    #Gives the possibility of creating a palindrome
    odd_count = 0
    odd_char = ""
    
    for char, freq in char_freq.items():
        if freq % 2 != 0:
            odd_count += 1 
            odd_char = char
    
    return odd_count <= 1, odd_char

def create_palindrome(char_freq):
    palindrome_true, odd_char = is_palindrome(char_freq)
    left_half = []
    
    for char, freq in char_freq.items():
        left_half.extend([char]*(freq//2))

    middle = odd_char if odd_char else ""
    right_half = left_half[::-1]
        
    return "".join(left_half) + middle + "".join(right_half)

def convert_string(input_string):
    input_array = list(input_string)
    usable_array = []
    for element in input_array:
        if element.isalnum():
            usable_array.append(element.lower())
    return usable_array

def print_answer(input_string):
    #convert the string to usable input
    usable_array = convert_string(input_string)
    
    #check for empty String
    if not usable_array:
        print("The String is empty")
        return
    
    char_freq = character_count(usable_array)
    palindrome_possible, _ = is_palindrome(char_freq)

    #check for palindrome
    if palindrome_possible:
        print(input_string, "can be rearranged into a palindrome")
        print("The palindrome is : ", create_palindrome(char_freq))
    else:
        print(input_string, "cannot form a palindrome")
    
String1 = "abcaebc"
print_answer(String1)
