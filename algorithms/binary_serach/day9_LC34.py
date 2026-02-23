"""Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity."""

def first_and_last_position(array, target):
    
    def lower_bound(array, target):
        left = 0 
        right = len(array)
        
        while left < right:
            mid = left + (right - left)//2
            
            if array[mid] >= target:
                right = mid
            else:
                left = mid + 1 
        return left
        
    def upper_bound(array, target):
        left = 0 
        right = len(array)
        
        while left < right:
            mid = left + (right - left)//2
            
            if array[mid] > target:
                right = mid
            else:
                left = mid + 1 
        return left
        
    first = lower_bound(array, target)
    last = upper_bound(array, target) - 1 
    
    if first == len(array) or array[first] != target:
        return [-1, -1]
    return [first, last]
    
nums = [5,7,7,8,8,10]
target = 8 

print(first_and_last_position(nums, target))
