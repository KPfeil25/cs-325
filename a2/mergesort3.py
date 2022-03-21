def merging(ogArr, low, firstThird, secondThird, high, arr):
    i = low # so we can increment these variables and not lose the values
    j = firstThird
    k = secondThird
    m = low
    while ((i < firstThird) and (j < secondThird) and (k < high)): # while we are still inside the bounds of the three created lists
        if ogArr[i] < ogArr[j]: # if element in the second is greater than the first
            if ogArr[i] < ogArr[k]: # greater in the third than the first
                arr[m] = ogArr[i] # assignemnt to new list
                m += 1 # increment
                i += 1
            else:
                arr[m] = ogArr[k] # else, assign it to the value in the second
                m += 1
                k += 1
        else:
            if ogArr[j] < ogArr[k]: # check the third & second, similar to the previous
                arr[m] = ogArr[j]
                m += 1
                j += 1
            else:
                arr[m] = ogArr[k]
                m += 1
                k += 1
        
    while ((i < firstThird) and (j < secondThird)): # when we are still in the bounds of the first two thirds
        if ogArr[i] < ogArr[j]: # check if the element in the second is greater
            arr[m] = ogArr[i] # if so, swap
            m += 1 # increment
            i += 1
        else:
            arr[m] = ogArr[j] # else, the element in the first is greater & assign values
            m += 1
            j += 1

    while ((j < secondThird) and (k < high)): # same as the code block above, but with the second and last thirds
        if ogArr[j] < ogArr[k]:
            arr[m] = ogArr[j]
            m += 1
            j += 1
        else:
            arr[m] = ogArr[k]
            m += 1
            k += 1

    while ((i < firstThird) and (k < high)): # again, same as the code block above but with the first and the last third
        if ogArr[i] < ogArr[k]:
            arr[m] = ogArr[i]
            m += 1
            i += 1
        else:
            arr[m] = ogArr[k]
            m += 1
            k += 1

    # ensuring that no elements were missed along the way
    while i < firstThird:
        arr[m] = ogArr[i]
        m += 1
        i += 1
    
    while j < secondThird:
        arr[m] = ogArr[j]
        m += 1
        j += 1

    while k < high:
        arr[m] = ogArr[k]
        m += 1
        k += 1

def merge3(ogArr, low, high, arr):
    if (high - low < 2): # check that the list is of the correct size
        return
    
    thirdOne = low + ((high - low) // 3) # calculate the upper bound of the first third
    thirdTwo = low + 2 * ((high - low) // 3) + 1 # calcualte the upper bound of the second third

    # recursive calls for all three sections of the list
    merge3(arr, low, thirdOne, ogArr)
    merge3(arr, thirdOne, thirdTwo, ogArr)
    merge3(arr, thirdTwo, high, ogArr)

    # merging the results back together
    merging(arr, low, thirdOne, thirdTwo, high, ogArr)

def mergeSort3Way(test, size):
    if size == 0:
        return
 
    # initialize the new list
    new_test = []

    # give it values so indexing is easier
    for h in range(0, size):
        new_test.append(test[h])

    # call the merge function
    merge3(new_test, 0, size, test)
    return new_test

# same as last assignment
fo = open("data.txt", "r") # open data.txt
lines = fo.readlines() # read in all of the lines
for line in lines:
    int_list = line.split(" ") # get rid of all of the spaces
    int_list2 = map(int, int_list) # convert them all into ints
    #print(int_list)
    num_nums = int(int_list[0]) # set the number of numbers
    num_list = []
    for i in range(1, num_nums + 1): # get all of the numbers and append them to this new list
        new_num = int(int_list[i])
        num_list.append(new_num)
    #print(num_list)
    new_list = mergeSort3Way(num_list, (len(num_list))) # sort
    print(*new_list, sep = " ") # print out the sorted lines
    #print(line)