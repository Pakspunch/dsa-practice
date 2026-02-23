# Remove duplicates for a sorted list

def remove_duplicates(input_list):
    boundary = 0
    for i in range(1, len(input_list)):
        if input_list[boundary] != input_list[i]:
            boundary += 1
            input_list[boundary] = input_list[i]
    return input_list[:boundary+1]

def empty_validation(input_list):
    return len(input_list) == 0
    
def print_answer(input_list):
    if empty_validation(input_list):
        print("There are no elements in the list ")
    else:
        print("The List without duplicates is : ", remove_duplicates(input_list))
    
listA = [1,2,2,3,4,4,5,5,5,6,7]
print_answer(listA)
