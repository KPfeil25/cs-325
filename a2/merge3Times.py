import time
from numpy import random
import csv

def merging(ogArr, low, firstThird, secondThird, high, arr):
    i = low
    j = firstThird
    k = secondThird
    m = low
    while ((i < firstThird) and (j < secondThird) and (k < high)):
        if ogArr[i] < ogArr[j]:
            if ogArr[i] < ogArr[k]:
                arr[m] = ogArr[i]
                m += 1
                i += 1
            else:
                arr[m] = ogArr[k]
                m += 1
                k += 1
        else:
            if ogArr[j] < ogArr[k]:
                arr[m] = ogArr[j]
                m += 1
                j += 1
            else:
                arr[m] = ogArr[k]
                m += 1
                k += 1
        
    while ((i < firstThird) and (j < secondThird)):
        if ogArr[i] < ogArr[j]:
            arr[m] = ogArr[i]
            m += 1
            i += 1
        else:
            arr[m] = ogArr[j]
            m += 1
            j += 1

    while ((j < secondThird) and (k < high)):
        if ogArr[j] < ogArr[k]:
            arr[m] = ogArr[j]
            m += 1
            j += 1
        else:
            arr[m] = ogArr[k]
            m += 1
            k += 1

    while ((i < firstThird) and (k < high)):
        if ogArr[i] < ogArr[k]:
            arr[m] = ogArr[i]
            m += 1
            i += 1
        else:
            arr[m] = ogArr[k]
            m += 1
            k += 1

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
    if (high - low < 2):
        return
    
    thirdOne = low + ((high - low) // 3)
    thirdTwo = low + 2 * ((high - low) // 3) + 1

    merge3(arr, low, thirdOne, ogArr)
    merge3(arr, thirdOne, thirdTwo, ogArr)
    merge3(arr, thirdTwo, high, ogArr)

    merging(arr, low, thirdOne, thirdTwo, high, ogArr)


def mergeSort3Way(test, size):
    if size == 0:
        return
 
    new_test = []

    for h in range(0, size):
        new_test.append(test[h])

    merge3(new_test, 0, size, test)
    return new_test

csv_file = open('merge3Times.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Size', 'Time'])

random.seed() # seed the random numbers
for i in range(0, 10):
    size = 200000 + (200000 * i) # same as insert for the rest
    nums = random.randint(10000, size=(size))
    t1 = time.time()
    new_list = mergeSort3Way(nums, size)
    t2 = time.time()
    diff = t2 - t1
    print(str(size) + " " + str(diff))
    csv_writer.writerow([size, diff])

csv_file.close()