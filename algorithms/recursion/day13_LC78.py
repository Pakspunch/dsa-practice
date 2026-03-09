"""Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

In subsets you always backtrack the last element added — the one at the end of current_set. 
pop() removes the last element by default."""

def subsets(input_set):
    result_set = []
    current_set = []
    index = 0
    def subsetmaker(current_set, index):
        if index == len(input_set):
            result_set.append(current_set[:])
            return
        current_set.append(input_set[index])
        subsetmaker(current_set, index + 1)
        current_set.pop()
        subsetmaker(current_set, index + 1)
    subsetmaker(current_set, index)
    return result_set

input_set = [1,2,3]
print(subsets(input_set))
