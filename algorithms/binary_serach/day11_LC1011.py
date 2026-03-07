import math

def shippingDays(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        current_load = 0
        maxDays = 1

        mid = (left + right)//2

        for weight in weights:
            if weight + current_load <= mid:
                current_load += weight
            else:
                current_load = weight
                maxDays += 1
        
        if maxDays <= days:
            right = mid
        else:
            left = mid + 1    
    return left

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(shippingDays(weights, days))