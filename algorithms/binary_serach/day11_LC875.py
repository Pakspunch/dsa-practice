"""Binary search doesn't only work on sorted arrays — it works on any monotonic decision space. 
The pattern is always the same — define your search space, write a check function, binary search over it, 
and when the check passes set right to mid because you're looking for the minimum valid value.

This exact pattern — minimum speed, minimum days, minimum capacity — shows up across a whole family of problems."""

import math

def kokolovesbanana(piles, h):
    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right)//2
        hours = sum(math.ceil(pile/mid) for pile in piles)

        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return left

piles = [3,6,7,11]
h = 8

print(kokolovesbanana(piles, h))