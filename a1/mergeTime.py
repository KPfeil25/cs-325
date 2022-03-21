import time
from numpy import random
import csv

def mergeSort(nums):
    if len(nums) > 1:

        mid = len(nums)//2 # find the center of nums for use next
 
        L = nums[:mid] # slice
        R = nums[mid:] # slice
 
        mergeSort(L) # recursive calls
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
    
csv_file = open('mergeTimes6.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Size', 'Time'])

random.seed() # seed the random numbers
for i in range(0, 10):
    size = 200000 + (200000 * i) # same as insert for the rest
    nums = random.randint(10000, size=(size))
    t1 = time.time()
    mergeSort(nums)
    t2 = time.time()
    diff = t2 - t1
    print(str(size) + " " + str(diff))
    csv_writer.writerow([size, diff])
    
csv_file.close()