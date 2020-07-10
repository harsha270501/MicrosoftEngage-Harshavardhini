
import graph as g
global walk

opt = []
walk=[]
endpt=[]
visit=[]

def block_node(blist):
    for i in range(g.dim[0] * g.dim[1]):
        walk.append(True)
        visit.append(False)

    for i in blist:

        walk[i] = False


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


    bestfs_search(e, visit, q, path)
    trace = []

    i = path[e][0]
    trace.append(e)
    while i != -1:
        trace.append(i)
        i = path[i][0]
    trace.reverse()
    return (trace,path[e][1])


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
