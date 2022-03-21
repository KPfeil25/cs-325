# looked through lecture slides to aid in writing the code

import time
from numpy import random
import csv

# recursive solution first

def Recursiveknapsack(weight, weight_arr, val_arr, length): 
   
    if length == 0 or weight == 0: 
        return 0
    
    if (weight_arr[length-1] > weight): 
        return Recursiveknapsack(weight, weight_arr, val_arr, length-1) 
  
    else: 
        return max(val_arr[length-1] + Recursiveknapsack(weight-weight_arr[length-1], weight_arr, val_arr, length-1), Recursiveknapsack(weight, weight_arr, val_arr, length-1))


# now the dynamic programming algorithm

def Dynamicknapsack(weight, weight_arr, val_arr, length): 
    table = [[0 for x in range(weight + 1)] for x in range(length + 1)] 
  
    for i in range(length + 1): 
        for j in range(weight + 1): 
            if i == 0 or weight == 0: 
                table[i][j] = 0
            elif weight_arr[i - 1] <= j: 
                table[i][j] = max(val_arr[i - 1] + table[i - 1][j-weight_arr[i - 1]], table[i - 1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
  
    return table[length][weight]

#csv_file = open('dynvsnumitems.csv', 'w')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['dyn_time', 'num_items'])

for k in range(0, 9):
    num_items = (k * 5) + 10
    total_weight = 100
    item_weights = random.randint(40, size=num_items) # max weight of 40
    item_vals = random.randint(60, size=num_items) # max value of 60
    recur_start = time.time() # start time for recursion
    rec_max = Recursiveknapsack(total_weight, item_weights, item_vals, num_items) # run alg, get max
    recur_end = time.time() # stop timer
    total_recur = recur_end - recur_start # find time taken to run the alg
    dyn_start = time.time()
    dyn_max = Dynamicknapsack(total_weight, item_weights, item_vals, num_items)
    dyn_end = time.time()
    total_dyn = dyn_end - dyn_start
    #csv_writer.writerow([total_dyn, num_items])
    print("N = " + str(num_items) + " W = " + str(total_weight) + " Rec time = " + str(total_recur) + " Dyn time = " + str(total_dyn) + " rec max = " + str(rec_max) + " dyn max = " + str(dyn_max))

#csv_file.close()