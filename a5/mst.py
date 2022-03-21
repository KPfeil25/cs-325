from math import sqrt

arr = []
def euclideandistance(x1, y1, x2, y2):
    dis = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return int(dis)

def printgraph(p,n,dist):
    total = 0
    print("Edges in MST ")
    print ("Point (x,y)                    distance")
    for i in range(1, n):
        print ('%-1s' % ' ','(',arr[p[i]][0],',',arr[p[i]][1],')', "-", '(',arr[i][0],',',arr[i][1],')', "\t", dist[i][p[i] ] )
        total += dist[i][p[i]]
    print('          Total distance        ',total)
def findminimum(k, visited,n):
    min = 99999
    for v in range(n):
        if k[v] < min and visited[v] == False:
            min = k[v]
            index = v

    return index

def prims(n,dist):
    k = [99999] * n
    p = [None] * n
    k[0] = 0
    visited = [False] * n

    p[0] = -1
    for i in range(n):
        u = findminimum(k, visited,n)
        visited[u] = True
        for v in range(n):
            if dist[u][v] > 0 and visited[v] == False and k[v] > dist[u][v]:
                k[v] = dist[u][v]
                p[v] = u

    printgraph(p,n,dist)

file = open("graph.txt","r")
contents = file.read().split('\n')
n = int(contents[0])

for i in range(0,n):
    x = contents[i+1]
    a = x.split(' ')
    x=int(a[0])
    y=int(a[1])
    arr.append([x,y])
dist = []
for i in range(n):
    temp = []
    for j in range(n):
        x1 = arr[i][0]
        y1 = arr[i][1]
        x2 = arr[j][0]
        y2 = arr[j][1]
        temp.append(euclideandistance(x1, y1, x2, y2))
    dist.append(temp)
  
prims(n,dist)