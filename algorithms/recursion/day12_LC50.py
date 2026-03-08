"""Implement pow(x, n), which calculates x raised to the power n"""

def powerOfNumber(number, power):
    if power == 0:
        return 1
    return round(number * powerOfNumber(number, power - 1), 5)

def powerOfNumbersquared(number, power):
    if power < 0:                                   #handles negative powers
        number = 1/number
        power = -power

    if power == 0:                                  #base case
        return 1

    half = powerOfNumbersquared(number, power//2)   #half function call

    if power % 2 == 0:                              #return condition for power
        return half * half
    else:
        return number * half * half
    

print(powerOfNumber(2.1, 3))
print(powerOfNumbersquared(2, -5))