from graph_tool.all import *
import maximum_induced_match as m_i_m
import dummy as dm
import os 



def graph_create(file_path , num, dirName) : 

	g = Graph(directed = False)

	file = open(file_path)
	# format check yap 

	a = file.readlines()
	list_of_edges = [None] * len(a)

	for i in range(len(a)) :
	    b = a[i].strip("\n").split(",")
	    #print(b[0],b[1]) 
	    list_of_edges[i] = [b[0],b[1]]

	vertices = {}

	for e in list_of_edges:
	    if e[0] not in vertices:
	        vertices[e[0]] = True
	    if e[1] not in vertices:
	        vertices[e[1]] = True


	name = [None] * len(vertices)

	i = 0

	for d in vertices:
	    vertices[d] = g.add_vertex()
	    name[i] = d
	    i += 1


	for edge in list_of_edges:
		g.add_edge(vertices[edge[0]], vertices[edge[1]])

	graph_tool.stats.remove_self_loops(g)

	if num == 2:
		l_heuristic = m_i_m.start(g, name, dirName)
	else:
		l_greedy = dm.start(g, name, dirName)

    #return l_heuristic, l_greedy, len(vertices), len(list_of_edges)