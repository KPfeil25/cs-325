import sys, math, time #sys to grab the command line args and math for rounding, time for timing

#euclidian distance formula from the assignment
def euclidian_distance(a, b):
    return round(math.sqrt((a[1] - b[1])**2 + (a[2] - b[2])**2), 0)

# initialize the arrays for the nodes
sol = []
nodes = []

file = open(sys.argv[1], "r")
for line in file.readlines():
    node = []
    for x in line.lstrip().rstrip().split(" "):
        #print(x)
        if len(x) == 0:
            #print("here")
            continue
        node.append(int(x))
    if (len(node) > 1):
        nodes.append(node)
        
sol.append(nodes[0]) # add the first node to select a place to start
nodes.remove(nodes[0])

t1 = time.time()

while nodes != []:

    current = sol[len(sol)-1] # use the node for the current spot in the list

    nearest = nodes[0]
    dist = 9999999999999 # create some arbitrary large distance
    for node in nodes:
        #print(node)
        #print(current)
        # if the node being checked is closest
        if euclidian_distance(node, current) < dist:
            nearest = node
            dist = euclidian_distance(node, current)

    sol.append(nearest) # add to the solution
    nodes.remove(nearest) # removes from nodes (this allows the loop to end correctly)


tour_len = 0
# add up all of the distances
for num in range (0, len(sol)-1):
    tour_len += euclidian_distance(sol[num], sol[num + 1])
tour_len += euclidian_distance(sol[0], sol[len(sol)-1])

#t2 = time.time()
#total = t2 - t1
#print("time = " + str(total))

print(sys.argv[1], int(tour_len)) # print the file and the calculated distance


file = open(sys.argv[1] + ".tour", "w") # open the file to write to
file.write(str(int(tour_len))) # write the first line
for num in sol: # write all of the cities
    file.write("\n")
    file.write(str(int(num[0]))) # choose index zero so it is the cities identifier
file.write("\n")
file.close()