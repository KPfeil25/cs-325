# source: https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
# this was used to understand the logic within selectactivities()
# simple bubblesort to work with a 2d array
def bubblesort(arr):
    l = len(arr) 
    for i in range(0, l-1): 
        for j in range(0, l-i-1): 
            if (arr[j][1] > arr[j + 1][1]): # checking the rows near each other in the second idx
                temp = arr[j] # create temp
                arr[j]= arr[j + 1] # swap
                arr[j + 1]= temp # swap pt. 2
    return arr

def selectactivities(array):
    #print("UNSORTED:")
    #print(*array, sep=" ")
    bubblesort(array)
    #print("SORTED:")
    #print(*array, sep=" ")
    tmp = []
    print("The following activities are selected")
    i = len(array) - 1
    tmp.append(array[i][0]) # add the first in the array to the solution because this is a greedy algorithm
    #enumerate(array)
    for index, j in reversed(list(enumerate(array))): # reverse and add the indexes back w/ enumerate
        if j[2] <= array[i][1]: # if the activity fits
            tmp.append(j[0]) # append
            i = index
    return list(reversed(tmp)) # return reversed so as to meet the assignment requirements

inF = open("act-2.txt") # open the file
tmp = [] # create the array to store the solution
num_set = 1 # tracking the number of the set of activities
for line in inF:
    line = line.rstrip() # remove all spaces (default since char wasnt specified)
    if ' ' not in line and len(tmp) > 0: # checking where the number of activities in the set starts
        print("Set: " + str(num_set)) # print the number of the set
        if(len(tmp[0]) <= 1):# if the tmp has results
            result = selectactivities(tmp[1:]) # add them after the first index
        else:
            result = selectactivities(tmp[0:]) # otherwise, add then after the second index
        result_len = len(result) # store the result
        print("Number of activities selected = " + str(result_len))
        res = str(result)[1:-1] # list slicing to get rid of the brackets
        print("Activities: " + res + '\n')
        num_set += 1 # increase the number of the set
        tmp = [] # reset temp
    else:
        tmp.append([int(j) for j in line.split()]) # actual data points (num, start, finish) are appended

if len(tmp) > 0: # ensure that the tmp is empty
    print("Set: " + str(num_set)) # print the set
    result = selectactivities(tmp)
    res = str(result)[1:-1] # list slicing again
    print("Number of activities selected = " + str(len(result)))
    print("Activities: " + res + '\n')