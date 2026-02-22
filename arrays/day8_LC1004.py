"""LeetCode 1004 — Max Consecutive Ones III
Problem Statement

You are given:
A binary array nums (only 0s and 1
An integer k
You can flip at most k zeros to 1s.
Return the maximum number of consecutive 1s in the array after flipping at most k zeros"""

#Find the longest subarray containing at most k zeros.
#Variable-size sliding window

def flip_zeros(input_array, zeroes):
    left, max_length, zero_count = 0, 0, 0 
    
    for right in range(len(input_array)):
        
        if input_array[right] == 0:
            zero_count += 1 
        
        while zero_count > zeroes:
            if input_array[left] == 0:
                zero_count -= 1 
            left += 1 
        
        max_length = max(max_length, right - left + 1)
    return max_length
    
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(flip_zeros(nums, k))
