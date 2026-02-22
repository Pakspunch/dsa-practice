"""Leetcode 567: Permutation in String:
Given twi strings s1 and s2, return true if permutation of s1 exists in s2.

Rewritten clearly:

Does s2 contain any substring of length len(s1)
whose character frequency matches s1?

Fixed-size sliding window + frequency comparison"""

from collections import Counter

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    need = Counter(s1)
    window = Counter()
    
    left = 0
    required = len(need)
    formed = 0
    
    for right in range(len(s2)):
        char = s2[right]
        window[char] += 1 
        if char in need and window[char] == need[char]:
            formed += 1 
        
        if right - left + 1 > len(s1):
            left_char = s2[left]
            if left_char in need and window[left_char] == need[left_char]:
                formed -= 1 
            window[left_char] -= 1 
            left += 1 
        
        if formed == required:
            return True
    return False

string1 = "ab"
string2 = "abbcbaddacba"
print(check_inclusion(string1,string2))
