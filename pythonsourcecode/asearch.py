# module - for A* search
# imports graph module
import graph as g

# list walk- specifies if each cell is walkable or not
walk = []
# list opt - specifies the options opted. opt[0]- option for Diagonal Movement, opt[1]- heuristics option if any
opt = []
# list endpt - endpt[0]- cell number , endpt[1] - x coordinate , endpt[2] - y coordinate
endpt=[]

# Function block_node changes the corresponding 'walk' value
# @param blist - list of nodes that needs to be blocked
def block_node(blist):
    for i in range(g.dim[0]*g.dim[1]):
        walk.append(True)

    for i in blist:
        walk[i] = False

# Function a_path calls the a_search function and traces back the path
# @param option - list of options
# @param s - start cell
# @param e - end cell
# @param blist - list of nodes that needs to be blocked
# @return (trace,distance) - returns trace list and total distance on a successful search
#                            else returns "Not Found"
def a_path(options, s, e, blist):
    block_node(blist)
    #vertices : src, f, g, h
    opt.append(options[0])
    opt.append(options[1])
    i=e//g.dim[1]
    j=e%g.dim[1]
    endpt.append(e)
    endpt.append(i)
    endpt.append(j)
    open_list={}
    open_list[s]=[-1,0,0,0]
    closed_list={}
    a=a_search(open_list,closed_list)
    if(a==-1):
        return "Not Found"
    trace=[e]
    p=closed_list[e]
    while(p!=-1):
        trace.append(p)
        p=closed_list[p]
    trace.reverse()
    return (trace,open_list[e][2])

# Function a_search - performs the A* Search Algorithm
# @param o - open list consists of the adjacent cells that are yet to be visited
# @param c - closed list that contains the cells that have been visited
# @return - returns 0 if successful else returns -1
def a_search(o, c):

    while (len(o.keys())!=0):

        val=o.values()

        mind=float('inf')
        minv=-1
        for i in o:
            if(o[i][1]<mind):
                mind=o[i][1]
                minv=i
        c[minv] = o[minv][0]
        if(minv==endpt[0]):
            return 0
        adj=g.get_neigh(minv,walk,opt[0])
        for i in adj:
            if i in c.keys():
                continue
            gd = o[minv][2] + g.edgelist[(minv, i)]

            if(i in o.keys()):
                if(gd<o[i][2]):
                    o[i][2]=gd
                    o[i][1]=o[i][2]+o[i][3]
            else:
                l=[]
                x = i // g.dim[1]
                y = i % g.dim[1]
                h1=g.calc_dist(endpt[1],endpt[2],x,y,opt[1])
                l=[minv,gd+h1,gd,h1]
                o[i]=l
        if minv == -1:
            return -1
        del o[minv]


