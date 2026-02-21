"""📘 Problem Statement
🔹 First Negative Integer in Every Window of Size K Given:
An integer array arr[] of size n
An integer k

Task:
For every contiguous subarray (window) of size k,
find the first negative integer in that window.

If a window does not contain a negative number, return 0 for that window."""

"""Fixed-size sliding window
+ selective tracking using deque"""

#Just track “interesting” elements (negatives) or In a moving time window, detect the first occurrence of a certain condition.
from collections import deque

def detect_first_negatives(arr, k):
    dq = deque()
    res = []
    
    for i, x in enumerate(arr):
        if x<0:
            dq.append(i)
        
        if dq and dq[0] <= i-k:
            dq.popleft()
        
        if i >= k-1:
            res.append((arr[dq[0]]) if dq else 0)
    
    return res
    
ListA = [-1, 2, 3,-5, 2,-7, 7, 9,-1]
k = 3

print(detect_first_negatives(ListA, k))
