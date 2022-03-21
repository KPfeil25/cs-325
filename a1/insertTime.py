import time
from numpy import random
import csv # needed to write to the files

# all of the commented out csv code was used to make my analysis either, but I dont imagine
# that you want some random csv files on your machine

def insertionSort(nums): 
    for i in range(1, len(nums)):
        key = nums[i] # current element
        j = i - 1 #check index
        while j >= 0 and key < nums[j]: 
                nums[j + 1] = nums[j] 
                j -= 1
        nums[j + 1] = key

#csv_file = open('insertTimes.csv', 'w')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['Size','Time'])

random.seed() # seed the random numbers
for i in range(0, 8):
    size = 2500 + (2500 * i) # used to make sizes 2500 to 20,000 by 2500
    nums = random.randint(10000, size=(size)) # use this to fill the list
    t1 = time.time() # start timer
    insertionSort(nums) #sort
    t2 = time.time() # stop timer
    diff = t2 - t1 #calculate time
    print(str(size) + " " + str(diff)) #print to console
    #csv_writer.writerow([size, diff])

#csv_file.close()