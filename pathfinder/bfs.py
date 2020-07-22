# module - for breadth first search
# imports graph module
from . import graph as g
global walk

# list opt - specifies the options opted. opt[0]- option for Diagonal Movement, opt[1]- heuristics option if any
opt = []
# list walk- specifies if each cell is walkable or not
walk=[]
# list visit - specifies if the cell has been already visited or not
visit=[]


# Function block_node changes the corresponding 'walk' and 'visit' value
# @param blist - list of nodes that needs to be blocked
def block_node(blist):
    
    for i in range(g.dim[0]*g.dim[1]):
        walk.append(True)
        visit.append(False)
    
    for i in blist:
        walk[i] = False


# Function bfs_path calls the bfs_search function and traces back the path
# @param option - list of options
# @param s - start cell
# @param e - end cell
# @param blist - list of nodes that needs to be blocked
# @return (trace,distance) - returns trace list and total distance on a successful search
#                            else returns -1

def bfs_path(option,s,e,blist):
    walk.clear()
    opt.clear()
    visit.clear()
    block_node(blist)

    opt.append(option[0])

    path = {}
    path[s] = [-1,0]
    q = []
    visit[s]=True
    q.append(s)

    b=bfs_search(e, q, path)
    if b == -1:
        return -1
    trace = []
    i = path[e][0]
    trace.append(e)
    trace.append(i)
    while i != -1:
        i = path[i][0]
        trace.append(i)
    trace.reverse()
    del trace[0:1]
    return [trace,path[e][1]]


# Function bfs_search - performs the Breadth First Search
# @param e - end cell number
# @param q - bfs queue
# @param p - path traced (cell number : (parent cell number, distance)
# @return - returns 0 if successful else returns -1

def bfs_search(e,q,p):
    l = len(q)

    if len(q) == 0:
        return -1
    for i in range(l):
        if q[i] == e:
            return 0
        visit[q[i]] = True

        adj = g.get_neigh(q[i], walk, opt[0])

        for j in adj:

            if visit[j] == False:
                d = g.edgelist[(q[i],j)] + p[q[i]][1]
                p[j]=[q[i],d]
                q.append(j)
                visit[j]=True

    del q[0:l]
    return bfs_search(e, q,  p)
    return -1
