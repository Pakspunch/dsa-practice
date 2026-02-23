def max_element_with_constraint(input_list):
    max_element = input_list[0]
    for elements in input_list:
        if elements > max_element:
            max_element = elements
             
    return max_element

def validation(input_list):
    if input_list == []:
        return True 
    
def print_answer(input_list):
    if validation(input_list):
        print("There are no elements in the list")
    else:
        print("The Maximum number is : ", max_element_with_constraint(input_list))
    
ListA = [-9, 0, 8, 5, 10, 9, -6, 1]
print_answer(ListA)
