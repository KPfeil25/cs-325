import time

def mergeSort(nums):
    if len(nums) > 1:

        mid = len(nums)//2 # find the center of nums for use next
 
        L = nums[:mid] # slice
        R = nums[mid:] # slice
 
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
 
        # sorting
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        # ensuring all elements are accounted for
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
# this process is all the same as insertsort.py, refer to those comments
fo = open("data.txt", "r")
lines = fo.readlines()
for line in lines:
    int_list = line.split(" ")
    int_list2 = map(int, int_list)
    #print(int_list)
    num_nums = int(int_list[0])
    num_list = []
    for i in range(1, num_nums):
        new_num = int(int_list[i])
        num_list.append(new_num)
    #print(num_list)
    mergeSort(num_list)
    print(*num_list, sep = " ")
    #print(line)
