def find_target_opt(input_list, target_num):
    seen = {}
    
    for i in range(len(input_list)):
        current_num = input_list[i]
        required_num = target_num - current_num
        
        if required_num in seen:
            print(current_num, input_list[seen[required_num]])
            pass
        seen[current_num] = i

find_target_opt(listA, target)
