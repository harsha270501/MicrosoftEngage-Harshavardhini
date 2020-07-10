import math
global nodelist, edgelist
global dim
global diagmov

# nodelist stores the each cell in the grid
# (x,y) : cell number
nodelist = {}

# edgelist stores the edges with distance(Euclidean) as the cost
# (cell no1, cell no2) :distance
edgelist = {}

# dim is store the dimensions of the grid layout
# dim[0] - row
# dim[1] - column
dim=[]

# Function add_node is to add the cell and cell number to the nodelist
# @param i - x position
# @param j - y position
# @param n - grid number

def add_node(i,j,n):
	v=(i,j)
	nodelist[v]=n

# Function add_edge is to add the edge to the edgelist
def add_edge():

    r = dim[0]
    c = dim[1]
    for pt in nodelist:
        p1=[]
        for j in pt:
            p1.append(j)
        i = p1[0]
        j = p1[1]

        # upper adjacent cell
        if i >= 1:
            x = i - 1
            y = j
            e = (nodelist[pt], nodelist[(x, y)])
            d = calc_dist(x,y,i,j)
            edgelist[e]=d

        # right adjacent cell
        if j <= c - 2:
            x = i
            y = j + 1
            e = (nodelist[pt], nodelist[(x, y)])
            d = calc_dist(x,y,i,j)
            edgelist[e] = d

        # lower adjacent cell
        if i <= r - 2:
            x = i + 1
            y = j
            e = (nodelist[pt], nodelist[(x, y)])
            d = calc_dist(x,y,i,j)
            edgelist[e] = d

        # left adjacent cell
        if j >= 1:
            x = i
            y = j - 1
            e = (nodelist[pt], nodelist[(x, y)])
            d = calc_dist(x,y,i,j)
            edgelist[e] = d

        # upper left diagonal cell
        if i >= 1 and j >= 1:
            x = i - 1
            y = j - 1
            e = (nodelist[pt], nodelist[(x, y)])
            d = calc_dist(x,y,i,j)
            edgelist[e] = d

        # upper right diagonal cell
        if i >= 1 and j <= c-2:
            x = i - 1
            y = j + 1
            e = (nodelist[pt], nodelist[(x, y)])
            d = calc_dist(x,y,i,j)
            edgelist[e] = d

        # lower right diagonal cell
        if i <= r-2 and j <= c-2:
            x = i + 1
            y = j + 1
            e = (nodelist[pt], nodelist[(x, y)])
            d = calc_dist(x,y,i,j)
            edgelist[e] = d

        # lower left diagonal cell
        if i <= r-2 and j >= 1:
            x = i + 1
            y = j - 1
            e = (nodelist[pt], nodelist[(x, y)])
            d = calc_dist(x,y,i,j)
            edgelist[e] = d

# Function to create a grid and calls the add_node function and add_edge function
# @param row - the number of rows
# @param col - the number of columns
def add_matrix(row,col):

    dim.append(row)
    dim.append(col)
    n=0
    for i in range(row):
        for j in range(col):
            add_node(i,j,n)
            n+=1
    add_edge()

# Function that returns the neighbours of the given point
# @param n - cell number
# @param walk - list that specifies if the cell number is walkable or not
# @opt - Option for the Diagonal Movement {0:Never, 1:Only when no obstacles, 2:If at most one obstacle, 3:Always}
def get_neigh(n, walk, opt):
    r = dim[0]
    c = dim[1]
    i = n // c
    j = n % c

    neigh = []
    t0 = False
    t1 = False
    t2 = False
    t3 = False

    if i >= 1:
        s0 = nodelist[(i - 1, j)]
        if walk[s0]:
            t0 = True
            neigh.append(s0)

    if j <= c - 2:
        s1 = nodelist[(i, j + 1)]
        if walk[s1]:
            t1 = True
            neigh.append(s1)

    if i <= r - 2:
        s2 = nodelist[(i + 1, j)]
        if walk[s2]:
            t2 = True
            neigh.append(s2)

    if j >= 1:
        s3 = nodelist[(i, j - 1)]
        if walk[s3]:
            t3 = True
            neigh.append(s3)

    if opt == 0:
        return neigh
    elif opt == 1:
        if t0 and t3:
            if i >= 1 and j >= 1:
                d0 = nodelist[(i - 1, j - 1)]
                if walk[d0]:
                    neigh.append(d0)
        if t0 and t1:
            if i >= 1 and j <= c - 2:
                d1 = nodelist[(i - 1, j + 1)]
                if walk[d1]:
                    neigh.append(d1)
        if t1 and t2:
            if i <= r - 2 and j <= c - 2:
                d2 = nodelist[(i + 1, j + 1)]
                if walk[d2]:
                    neigh.append(d2)
        if t2 and t3:
            if i <= r - 2 and j >= 1:
                d3 = nodelist[(i + 1, j - 1)]
                if walk[d3]:
                    neigh.append(d3)
        return neigh

    elif opt == 2:

        if t0 or t3:
            if i >= 1 and j >= 1:
                d0 = nodelist[(i - 1, j - 1)]
                if walk[d0]:

                    neigh.append(d0)
        if t0 or t1:
            if i >= 1 and j <= c - 2:
                d1 = nodelist[(i - 1, j + 1)]
                if walk[d1]:

                    neigh.append(d1)
        if t1 or t2:

            if i <= r - 2 and j <= c - 2:

                d2 = nodelist[(i + 1, j + 1)]

                if walk[d2]:
                    neigh.append(d2)
        if t2 or t3:
            if i <= r - 2 and j >= 1:
                d3 = nodelist[(i + 1, j - 1)]

                if walk[d3]:
                    neigh.append(d3)
        return neigh

    else:
        if i >= 1 and j >= 1:
            d0 = nodelist[(i - 1, j - 1)]
            if walk[d0]:
                neigh.append(d0)
        if i >= 1 and j <= c-2:
            d1 = nodelist[(i - 1, j + 1)]
            if walk[d1]:
                neigh.append(d1)
        if i <= r-2 and j <= c-2:
            d2 = nodelist[(i + 1, j + 1)]
            if walk[d2]:
                neigh.append(d2)
        if i <= r-2 and j >= 1:
            d3 = nodelist[(i + 1, j - 1)]
            if walk[d3]:
                neigh.append(d3)
        return neigh

# Function calc_dist - calculates distance between two points
# @param x1 - x coordinate of the first point
# @param y1 - y coordinate of the first point
# @param x2 - x coordinate of the second point
# @param y2 - y coordinate of the second point
def calc_dist(x1,y1,x2,y2,opt=0):
    d=0
    if opt == 0 :
        d = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    elif opt == 1:
        d=abs(x2-x1)+abs(y2-y1)
    return d