import graph as g

walk = []
dist = {}
opt = []
walk = []

endpt=[]

def block_node(blist):
    for i in range(g.dim[0] * g.dim[1]):
        walk.append(True)

    for i in blist:
        walk[i] = False


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

def ida_search(path, g1, bound):
    n=path[-1][0]
    f=g1+g.calc_dist(n//g.dim[1],n%g.dim[1],endpt[1],endpt[2],opt[1])
    if(f>bound):
        return f
    if(n==endpt[0]):
        return "Found"
    mind=float('inf')
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
            path.pop()
    return mind



