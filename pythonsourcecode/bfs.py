
import graph as g
global walk

opt = []
walk=[]
visit=[]

def block_node(blist):

    for i in range(g.dim[0]*g.dim[1]):
        walk.append(True)
        visit.append(False)
    for i in blist:
        walk[i] = False


def bfs_path(option,s,e,blist):

    block_node(blist)
    opt.append(option)

    path = {}
    path[s] = [-1,0]
    q = []
    visit[s]=True
    q.append(s)

    bfs_search(e, visit, q, path)
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


def bfs_search(e,v,q,p):
    l = len(q)

    if len(q) == 0:
        return -1
    for i in range(l):
        if q[i] == e:
            return 0
        v[q[i]] = True

        adj = g.get_neigh(q[i], walk, opt[0])

        for j in adj:

            if v[j] == False:
                d = g.edgelist[(q[i],j)] + p[q[i]][1]
                p[j]=[q[i],d]
                q.append(j)
                v[j]=True

    del q[0:l]
    bfs_search(e, v, q,  p)
    return -1
