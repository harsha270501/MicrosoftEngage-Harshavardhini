# module - for IDA* search
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
    for i in range(g.dim[0] * g.dim[1]):
        walk.append(True)

    for i in blist:
        walk[i] = False

# Function a_path calls the a_search function and traces back the path
# @param option - list of options
# @param s - start cell
# @param e - end cell
# @param blist - list of nodes that needs to be blocked
# @return (trace,distance) - returns path if successful
#                            else returns "Not Found"
def ida_path(options, s, e, blist):
    block_node(blist)
    #vertices : src, f, g, h
    opt.append(options[0])
    opt.append(options[1])
    i=e//g.dim[1]
    j=e%g.dim[1]
    endpt.append(e)
    endpt.append(i)
    endpt.append(j)
    bound=g.calc_dist(s//g.dim[1],s%g.dim[1],i,j,opt[1])
    path=[[s,0]]
    f=0
    g1=0
    while(1):
        t=ida_search(path,g1,bound)
        if t == "Found":
            f=1
            break
        elif t == "Not Found":
            return "Not Found"
        bound=t
    if(f==0):
        return "Not Found"
    return path

# Function a_search - performs the A* Search Algorithm
# @param path - path traced (list where each element is (cell number,distance))
# @param g1 - distance traversed so far
# @param bound - the bound value for comparison
# @return - returns "Found" if the end point is reached
#           else returns the new bound
#           returns "Not Found" if the end point can't be reached
def ida_search(path, g1, bound):
    n=path[-1][0]
    f=g1+g.calc_dist(n//g.dim[1],n%g.dim[1],endpt[1],endpt[2],opt[1])
    if(f>bound):
        return f
    if(n==endpt[0]):
        return "Found"
    mind=float('inf')
    minv=-1
    adj=g.get_neigh(n,walk,opt[0])
    for i in adj:
        if i not in path:
            g2=g1+g.edgelist[(n,i)]
            path.append([i,g2])
            t=ida_search(path,g2,bound)
            if t == "Found":
                return "Found"
            if t < mind:
                mind=t
                minv=i
            path.pop()
    if minv == -1:
        return "Not Found"
    else:
        return mind



