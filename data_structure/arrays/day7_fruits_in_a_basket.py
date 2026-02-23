"""Problem: Fruits Into Baskets

Problem Statement
You are given an integer array fruits, where:
Each number represents a type of fruit.
You have only 2 baskets.
Each basket can hold only one type of fruit.
You can pick fruits from a contiguous subarray.

Task:
Return the maximum number of fruits you can collect."""

#Find the length of the longest subarray containing at most 2 distinct elements.
#Variable-size sliding window + frequency map

from collections import defaultdict

def total_fruits(fruits):
    
    count = defaultdict(int)
    left = 0 
    max_length = 0
    
    start = 0
    
    for right in range(len(fruits)):
        count[fruits[right]] += 1 
        
        while len(count) > 2:
            count[fruits[left]] -= 1 
            
            if count[fruits[left]] == 0:
                del count[fruits[left]]
                
            left += 1 
        
        curr_length = right - left  + 1 
        #max_length = max(max_length, curr_length)
        
        if curr_length > max_length:
            max_length = curr_length
            start = left
            
    return max_length, fruits[start : start + max_length]
    
fruits = [1, 2, 3, 2, 2]
print(total_fruits(fruits))
