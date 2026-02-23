def sum_of_list(input_list):
    list_sum = 0
    for element in input_list:
        list_sum += element
    return list_sum
    
def maximum_num(input_list):
    max_num = input_list[0]
    for element in input_list:
        if element > max_num:
            max_num = element
    return max_num
    
def even_num(input_list):
    count = 0
    for element in input_list:
        if element % 2 ==0:
            count += 1
    return count
    
def reverse_list(input_list):
    reversed_list = list(reversed(input_list))
    return reversed_list
    
def list_traversal(input_list):
    for element in input_list:
        print("The traversed element in the list is : ", element)

def print_answer(input_list):
    print("Total sum of elements in the list is : ", sum_of_list(input_list))
    print("The maximum number in the list is : ", maximum_num(input_list))
    print("The total number of even numbers : ", even_num(input_list))
    print("The reversed list is : ", reverse_list(input_list))
    print(list_traversal(input_list))
    
def validation(input_list):
    if input_list == []:
        return "No elements in the List"
    else:
        return print_answer(input_list)
    

listA =[-2,4-9,10,0,45]
validation(listA)
