# file for testing the algorithms
import graph as g
import bfs
import dijkstra
import asearch
import idasearch
import bestfirstsearch

def main():
	g.add_matrix(6, 6)
	print("Breadth First Search: ")
	b=bfs.bfs_path(2, 7, 29, [3, 4, 9, 16, 20, 21, 25])
	if b == "Not Found":
		print("Path not found")
	else:
		for x in b:
			print(x)

	print("Dijkstra Search: ")
	d=dijkstra.dijkstra_path(1, 7, 29, [3, 4, 9, 16, 20, 21, 25])
	if d == "Not Found":
		print("Path not found")
	else:
		for x in d:
			print(x)

	print("A* Search Algorithm: ")
	a=asearch.a_path([1, 1], 7, 29, [3, 4, 9, 16, 19, 20, 21, 25])
	if a == "Not Found":
		print("Path Not Found")
	else:
		for x in a:
			print(x)

	print("IDA* Search Algorithm: ")
	ida= idasearch.ida_path([2, 1], 7, 29, [3, 4, 9, 16, 19, 20, 21, 25])
	if ida == "Not Found":
		print("Path Not Found")
	else:
		idap=[]
		for x in ida:
			idap.append(x[0])
		print(idap)
		print(ida[-1][1])

	print("Best first Search")
	bestfs=bestfirstsearch.bestfs_path([2, 1], 7, 29, [3, 4, 9, 16, 20, 21, 25])
	if bestfs == "Not Found":
		print("Path Not FOund")
	else:
		for x in bestfs:
			print(x)

if(__name__=='__main__'):
	main()
