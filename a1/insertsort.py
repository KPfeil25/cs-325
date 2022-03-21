import time

def insertionSort(nums): 
    for i in range(1, len(nums)): 
        key = nums[i] 
        j = i - 1
        while j >= 0 and key < nums[j]: 
                nums[j + 1] = nums[j] 
                j -= 1
        nums[j + 1] = key

fo = open("data.txt", "r")
lines = fo.readlines() # grab all of the lines
for line in lines:
    int_list = line.split(" ") # split by space
    int_list2 = map(int, int_list) # convert to ints
    #print(int_list)
    num_nums = int(int_list[0]) # this one is the size
    num_list = []
    for i in range(1, num_nums):
        new_num = int(int_list[i]) # make the current index an int
        num_list.append(new_num) # add to list
    #print(num_list)
    insertionSort(num_list) # sort
    print(*num_list, sep = " ") # print
    #print(line)