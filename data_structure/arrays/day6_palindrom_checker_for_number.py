def is_number_palindrome(x):
    #convert int to list
    num = []
    if x == 0:
        num = [0]
    sign = -1 if x < 0 else 1
    input_number = abs(x)

    while input_number > 0:
        num.append(input_number%10)
        input_number//=10

    num.reverse()
    num[0] *= sign

    #check for palindrome
    if len(num) > 0 and num[0] < 0:
        return False

    left = 0
    right = len(num) - 1 
    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    
    return True

input_number1 = 121
print(is_number_palindrome(input_number1))
