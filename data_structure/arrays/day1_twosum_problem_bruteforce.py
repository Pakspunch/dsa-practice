def find_target(input_list, target_num):
    for i in range(0, len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] + input_list[j] == target_num:
                print(input_list[i], input_list[j])

listA = [1,4,2,5,-2,8,10,-4,0,1,6]
target = 6

find_target(listA,target)
