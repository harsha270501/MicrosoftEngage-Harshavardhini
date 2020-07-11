# module - for dijkstra search
# imports graph module

import graph as g

# list walk- specifies if each cell is walkable or not
walk = []
# list opt - specifies the options opted. opt[0]- option for Diagonal Movement, opt[1]- heuristics option if any
opt = []

# Function block_node changes the corresponding 'walk' value
# @param blist - list of nodes that needs to be blocked
def block_node(blist):
    for i in range(g.dim[0]*g.dim[1]):
        walk.append(True)

    for i in blist:
        walk[i] = False


# Function dijkstra_path calls the dijkstra_search function and traces back the path
# @param option - list of options
# @param s - start cell
# @param e - end cell
# @param blist - list of nodes that needs to be blocked
# @return (trace,distance) - returns trace list and total distance on a successful search
#                            else returns -1

def dijkstra_path(option, s, e, blist):
    block_node(blist)
    opt.append(option)
    path={}
    #vertex no: src , dist , visited
    path[s]=[-1,0,True]
    d=dijkstra_search(e,s,path)

    if d == -1:
        return d
    trace = []
    i = path[e][0]
    trace.append(e)
    trace.append(i)
    while i != -1:
        i = path[i][0]
        trace.append(i)
    trace.reverse()
    del trace[0:1]
    return (trace,path[e][1])


# Function bfs_search - performs the Breadth First Search
# @param e - end cell number
# @param v - vertex whose neighbours for which edge relaxation has to be done.
# @param p - path traced (cell number : (parent cell number, distance)
# @return - returns 0 if successful else returns -1

def dijkstra_search(e,v,p):

    mind=float('inf')
    minv=-1
    adj=g.get_neigh(v,walk,opt[0])
    for i in adj:
        d = p[v][1] + g.edgelist[(v, i)]
        if i not in p.keys():
            l=[v,d,False]
            p[i]=l
        elif p[i][2] == False:
            if p[i][1] == -1 or d<p[i][1]:
                p[i][0] = v
                p[i][1] = d
    for i in p:
        if p[i][2] == False and p[i][1] != -1:
            if p[i][1]<mind:
                mind = p[i][1]
                minv = i
    if minv == -1:
        return -1
    p[minv][2]=True
    if minv == e:
        return 0
    return dijkstra_search(e, minv, p)
    return -1
