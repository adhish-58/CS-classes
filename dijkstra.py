#Adhish Adhikari
#Networks and Networking
#10/24/16

import sys
import copy

class Edges:
	def __init__(self, from_node, to_node, cost):
		self.from_node = from_node
		self.to_node = to_node
		self.cost = cost

def remove_u_from_unvisited_nodes (x, table):
	count = 0
	for i in table:
		if i == x:
			del table[count]
			return

		count += 1

def dijkstra(Graph, source_node, vertices):
		cost_value = {}
		previous_node = {}
		path_tracker = {}
		unvisited_nodes = []
		visted_nodes = []
		alt = 0

		for v in vertices:
			#print(v)
			cost_value[str(v)] = float('inf')
			previous_node[str(v)] = -1
			path_tracker[str(v)] = [source_node]
			unvisited_nodes.append(v)

		cost_value[str(source_node)] = 0
		path_tracker[str(source_node)].append(-1)

		while len(unvisited_nodes) != 0:
			u = None
			cost_from_u = float('inf')
			#print("cost is here")

			for i in unvisited_nodes:
				if cost_value[i] < cost_from_u:
					cost_from_u = cost_value[i]
					u = i

			remove_u_from_unvisited_nodes(u,unvisited_nodes)
			#print ("unvistied nodes:",unvisited_nodes)

			for g in Graph:
				#print ("edge:",g.from_node,g.to_node,g.cost)
				if u == g.from_node:
					alt = cost_value[str(u)] + int(g.cost)
					if int(alt) < cost_value[str(g.to_node)]:
						#print("change cost of:",g.to_node)
						cost_value[str(g.to_node)] = alt
						previous_node[str(g.to_node)] = g.to_node

						if u != source_node:
							path_tracker[g.to_node] = copy.deepcopy(path_tracker[u])
							#print("path of u before",path_tracker[u])
						path_tracker[g.to_node].append(g.to_node)
						#print("path of u after",path_tracker[u])

				elif u == g.to_node:
					#print ("for node 2", g.from_node,g.to_node,g.cost)
					alt = cost_value[str(u)] + g.cost
					if alt < cost_value[str(g.from_node)]:
						#print("cahnge cost of:",g.to_node)
						cost_value[str(g.from_node)] = alt
						previous_node[str(g.from_node)] = g.from_node

						if u != source_node:
							path_tracker[g.from_node] = copy.deepcopy(path_tracker[u])
							#print(path_tracker[u])
						path_tracker[str(g.from_node)].append(g.from_node)

			sorted_costs = sorted(cost_value)

		for c in sorted_costs:
			print("Dijkstra - ", "source: %s" % source_node, "destination: %s" % c, "route: %s" % path_tracker[c][1], "cost: %s" % cost_value[c])
		print()
		#print ("Dijkstra - source: ",source, "destination - ",c, "route - ", previous[c][1], "cost - ",distance[c])
		#print(path_tracker[c])

def exists(vertices, node):
	for j in vertices:
		if j == node :
			return True

	return False

def main():
	Graph = []
	vertices = []

	infile = open(sys.argv[1],"r")
	for line in infile :
		each_line = line.split(" ")
		Graph.append(Edges(each_line[0],each_line[1],int(each_line[2])))

	for g in Graph:
		if exists(vertices, g.from_node) == False:
			vertices.append(g.from_node)
		if exists(vertices, g.to_node) == False:
			vertices.append(g.to_node)

	vertices.sort()

	for v in vertices:
		dijkstra(Graph, v, vertices)

main()

"""
Dijkstra -  source: 0 destination: 0 route: -1 cost: 0
Dijkstra -  source: 0 destination: 1 route: 1 cost: 2
Dijkstra -  source: 0 destination: 2 route: 1 cost: 3
Dijkstra -  source: 0 destination: 3 route: 1 cost: 4

Dijkstra -  source: 1 destination: 0 route: 0 cost: 2
Dijkstra -  source: 1 destination: 1 route: -1 cost: 0
Dijkstra -  source: 1 destination: 2 route: 2 cost: 1
Dijkstra -  source: 1 destination: 3 route: 3 cost: 2

Dijkstra -  source: 2 destination: 0 route: 1 cost: 3
Dijkstra -  source: 2 destination: 1 route: 1 cost: 1
Dijkstra -  source: 2 destination: 2 route: -1 cost: 0
Dijkstra -  source: 2 destination: 3 route: 1 cost: 3

Dijkstra -  source: 3 destination: 0 route: 1 cost: 4
Dijkstra -  source: 3 destination: 1 route: 1 cost: 2
Dijkstra -  source: 3 destination: 2 route: 1 cost: 3
Dijkstra -  source: 3 destination: 3 route: -1 cost: 0
"""
