from django.shortcuts import render
from django.http import JsonResponse
from . import graph
from . import bfs
from . import dijkstra
from . import asearch
from . import idasearch
from . import bestfirstsearch
import json

# Create your views here.
def index(request):
    return render(request,'index.html');

def creategrid(request):
    graph.add_matrix(36,64)
    return JsonResponse({'Returnval':'True'})

def searchpath(request):
   
    s=int(request.POST.get('start'))
    
    bl=request.POST.getlist('blocked[]')
    blocked = list(map(int, bl))
    typ=request.POST.get('searchtype')
    ol=request.POST.getlist('options[]')
    o=list(map(int, ol))
    res='False'
    if(typ=="bfs"):
        e=request.POST.getlist('end[]')
        e=list(map(int,e))
        b=bfs.bfs_path(o,s,e,blocked)
        if b!="Not Found":
            res=b
        return JsonResponse({'Result':res});
    elif(typ=="dijkstra"):
        e=request.POST.getlist('end[]')
        e=list(map(int,e))
        d=dijkstra.dijkstra_path(o, s, e, blocked)
        if d!="Not Found":
            res=d
        return JsonResponse({'Result':res});
        
    elif(typ=="bestfirstsearch"):
        e=int(request.POST.get('end'))
        bestfs=bestfirstsearch.bestfs_path(o, s, e, blocked)
        if bestfs!="Not Found":
            x={}
            x['path']=bestfs[0]
            x['dist']=bestfs[1]
            print(x)
            res=x
        return JsonResponse({'Result':res});
    elif(typ=="Asearch"):
        e=int(request.POST.get('end'))
        a=asearch.a_path(o, s, e, blocked)
        if a!="Not Found":
            x={}
            x['path']=a[0]
            x['dist']=a[1]
            res=x
        return JsonResponse({'Result':res});
    elif(typ=="IDAsearch"):

        e=int(request.POST.get('end'))
        ida= idasearch.ida_path(o, s, e, blocked)
        if ida!="Not Found":
            x={}
            idap=[]
            for j in ida:
                idap.append(j[0])
            x['path']=idap
            x['dist']=ida[-1][1]
            res=x
        return JsonResponse({'Result':res});
    else:
        return JsonResponse({'Result':res});
