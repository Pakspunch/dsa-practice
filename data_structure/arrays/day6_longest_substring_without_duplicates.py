"""This problem teaches:

Dynamic sliding window
Hash map for last seen indices
Pointer control
Window shrinking logic
Why max(left, last_seen + 1) matters"""

def longest_substring_without_repitition(input_string):
    input_array = list(input_string)
    
    seen = {}
    left_index = 0
    max_length = 0
    best_window_index = 0
    
    for index, element in enumerate(input_array):
        if element in seen:
            left_index = max(left_index, seen[element] + 1 )
            
        current_window_length = index - left_index + 1  
        
        if current_window_length > max_length:
            best_window_index = left_index
            max_length = current_window_length
        
        seen[element] = index
        
    print(input_array[best_window_index: best_window_index + max_length])
    
String1 = "abcabcbb"
String2 = "pwwkew"
longest_substring_without_repitition(String1)
longest_substring_without_repitition(String2)
