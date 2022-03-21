import time
from numpy import random
import csv

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

#csv_file = open('merge3Times.csv', 'w')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['Size', 'Time'])

random.seed() # seed the random numbers
for i in range(0, 10):
    size = 200000 + (200000 * i) # create the size increments
    nums = random.randint(10000, size=(size)) # generate the random lists
    t1 = time.time() # start clock
    new_list = mergeSort3Way(nums, size) # sort
    t2 = time.time() # stop clock
    diff = t2 - t1 # calculate difference
    print(str(size) + " " + str(diff)) # output to the terminal
    #csv_writer.writerow([size, diff])

#csv_file.close()