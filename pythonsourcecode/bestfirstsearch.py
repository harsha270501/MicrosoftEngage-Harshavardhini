# module - for A* search
# imports graph module
import graph as g
global walk

# list opt - specifies the options opted. opt[0]- option for Diagonal Movement, opt[1]- heuristics option if any
opt = []
# list walk- specifies if each cell is walkable or not
walk=[]
# list endpt - endpt[0]- cell number , endpt[1] - x coordinate , endpt[2] - y coordinate
endpt=[]
# list visit - specifies if the cell has been already visited or not
visit=[]

# Function block_node changes the corresponding 'walk' and 'visit' value
# @param blist - list of nodes that needs to be blocked
def block_node(blist):
    for i in range(g.dim[0] * g.dim[1]):
        walk.append(True)
        visit.append(False)

    for i in blist:
        walk[i] = False

# Function bestfs_path calls the bestfs_search function and traces back the path
# @param option - list of options
# @param s - start cell
# @param e - end cell
# @param blist - list of nodes that needs to be blocked
# @return (trace,distance) - returns trace list and total distance on a successful search
#                            else returns "Not Found"
def bestfs_path(options,s,e,blist):

    block_node(blist)
    # vertices : src, f, g, h
    opt.append(options[0])
    opt.append(options[1])
    i = e // g.dim[1]
    j = e % g.dim[1]
    endpt.append(e)
    endpt.append(i)
    endpt.append(j)

    path = {}
    path[s] = [-1,0]
    q = [[s,g.calc_dist(endpt[1],endpt[2],s//g.dim[1],s%g.dim[1])]]
    visit[s]=True


    b=bestfs_search(e, visit, q, path)
    if b == -1:
        return "Not Found"
    trace = []
    i = path[e][0]
    trace.append(e)
    while i != -1:
        trace.append(i)
        i = path[i][0]
    trace.reverse()
    return (trace,path[e][1])

# Function bfs_search - performs the Breadth First Search
# @param e - end cell number
# @param v - cell v whose adjacent cells have to be explored
# @param q - best first search queue
# @param p - path traced (cell number : (parent cell number, distance)
# @return - returns 0 if successful else returns -1

def bestfs_search(e,v,q,p):
    l = len(q)

    if len(q) == 0:
        return -1
    minv=0


    for i in range(l):
        if(q[i][1]<q[minv][1]):
            minv=i
    vert=q[minv][0]

    if vert == e:
        return 0
    del q[minv:minv+1]
    adj=g.get_neigh(vert,walk,opt[0])

    for i in adj:
        if(v[i]==False):
            h=g.calc_dist(endpt[1],endpt[2],i//g.dim[1],i%g.dim[1],opt[1])
            q.append([i,h])
            v[i]=True
            p[i]=[vert,p[vert][1]+g.edgelist[(i,vert)]]

    return bestfs_search(e, v, q,  p)
    return -1
