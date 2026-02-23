def moving_zeroes(input_list):
    boundary = 0
    
    for i in range(len(input_list)):
        if input_list[i] != 0:
            input_list[boundary] = input_list[i]
            boundary += 1
        else:
            pass
        
    for j in range(boundary, len(input_list)):
        input_list[j] = 0
        
    print(input_list)

listA = [2,0,0,1,0,19]
moving_zeroes(listA)
