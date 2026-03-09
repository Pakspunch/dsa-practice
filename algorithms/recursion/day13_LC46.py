'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
In permutations you backtrack a specific element — the one you picked from remaining in that iteration. 
That element might not be at the end of the list after recursion unwinds. 
So you need remove(element) to target it specifically.'''

def permutation(input_set):
    result_set = []
    remaining_set = input_set
    current_set = []

    def findPermuatation(current_set, remaining_set):
        if not remaining_set:
            result_set.append(current_set[:])
            return
        for element in remaining_set[:]:
            current_set.append(element)
            remaining_set.remove(element)
            findPermuatation(current_set, remaining_set)
            current_set.remove(element)
            remaining_set.append(element)
    
    findPermuatation(current_set, remaining_set)
    return result_set

input_set = [1,2,3]
print(permutation(input_set))