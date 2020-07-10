import graph as g
import bfs
import dijkstra
import asearch
import idasearch
import bestfirstsearch

def main():
	g.add_matrix(6, 6)

	b=bfs.bfs_path(2, 7, 29, [3, 4, 9, 16, 20, 21, 25])
	for x in b:
		print(x)

	d=dijkstra.dijkstra_path(1, 7, 29, [3, 4, 9, 16, 20, 21, 25])
	if(d==-1):
		print(-1)
	else:
		for x in d:
			print(x)

	a=asearch.a_path([1, 1], 7, 29, [3, 4, 9, 16, 19, 20, 21, 25])
	for x in a:
		print(x)

	ida= idasearch.ida_path([2, 1], 7, 29, [3, 4, 9, 16, 19, 20, 21, 25])
	idap=[]
	for x in ida:
		idap.append(x[0])
	print(idap)
	print(ida[-1][1])

	print("Best first Search")
	bestfs=bestfirstsearch.bestfs_path([2, 1], 7, 29, [3, 4, 9, 16, 20, 21, 25])
	for x in bestfs:
		print(x)

if(__name__=='__main__'):
	main()
