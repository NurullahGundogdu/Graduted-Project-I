from graph_tool.all import *
import sys, os


class induced:
	def __init__(self, graph, vertex_name):
		self.graph = graph
		self.vertex_prop_int = graph.new_vertex_property("int",0)
		self.dict_induced = {}
		self.vertex_name = vertex_name
		self.dict_induced_real_name = {}

		self.vertex_color = graph.new_vertex_property("string")
		self.edge_color = graph.new_edge_property("string")

		for r in graph.vertices():
			self.vertex_color[r] = "#C133FF"

		arr = []

		for r in graph.edges():
			self.edge_color[r] = "#C133FF"
			arr.append(r)

def vertex_checker(object_graph):
	
	vertexes = object_graph.graph.get_vertices()

	for i in vertexes:
		if object_graph.vertex_prop_int[i] == 0:
			edge_checker(vertexes[i], object_graph)


def edge_checker(vertex, object_graph):
	
	edges = object_graph.graph.get_all_edges(vertex, [object_graph.graph.edge_index])

	for i in edges:

		if object_graph.vertex_prop_int[i[1]] == 0:
			object_graph.dict_induced[vertex] = i[1]
			object_graph.dict_induced_real_name[object_graph.vertex_name[vertex]] = object_graph.vertex_name[i[1]]
			change_prop_int(vertex, i[1], edges, object_graph)



def change_prop_int(vertex, edge, edges, object_graph):
	
	object_graph.vertex_prop_int[vertex] = 1
	object_graph.vertex_prop_int[edge] = 1

	object_graph.vertex_color[vertex] = "#5EFF33" 
	object_graph.vertex_color[edge] = "#5EFF33"

	for a in object_graph.graph.edges():
		b = list(a)
		if b[0] == vertex and b[1] == edge or b[1] == vertex and b[0] == edge:
			object_graph.edge_color[a] = "#5EFF33"


	for i in edges:
		if object_graph.vertex_prop_int[i[1]] == 0:
			object_graph.vertex_prop_int[i[1]] = 2

	temp = object_graph.graph.get_all_edges(edge, [object_graph.graph.edge_index])

	for i in temp:
		if object_graph.vertex_prop_int[i[1]] == 0:
			object_graph.vertex_prop_int[i[1]] = 2


def write_to_file_and_draw(object_graph, dirName, vertex_name):

	if not os.path.exists(dirName + "/Greedy"):
		os.mkdir(dirName + "/Greedy")

	graph_draw(object_graph.graph, vertex_fill_color = object_graph.vertex_color, vertex_font_size=20, output_size=(800, 800),  edge_color = object_graph.edge_color, vertex_text = vertex_name, output=dirName + "/Greedy/graph.png")	
	
	f = open(dirName + "/Greedy/matchs.txt", "w")

	f.write("Induced Match Number  :  ")
	f.write(str(len(object_graph.dict_induced)))
	f.write("\n\nMatches:\n\n")

	for i in object_graph.dict_induced_real_name.keys():
		f.write(i)
		f.write(", ")
		f.write(object_graph.dict_induced_real_name[i])
		f.write("\n")
	f.close()

	
	graph_draw(object_graph.graph, vertex_fill_color = object_graph.vertex_color, vertex_font_size=20, output_size=(800, 800),  edge_color = object_graph.edge_color, vertex_text = vertex_name)#, output=dirName + "/Heuristic/graph.png")


def start(g, name, dirName):
	
	vertex_name = g.new_vertex_property("string")


	i = 0
	
	for r in g.vertices():
		vertex_name[r] = name[i]
		i += 1
	
	
	
	#graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(2000, 2000), output="two-nodes.png")
	#vertex_prop_int = g.new_vertex_property("int",0)	# 0 not induced ------ 1 induced ----- 2 neighbor induced 
	
	object_graph = induced(g, vertex_name)

	

	vertex_checker(object_graph)

	write_to_file_and_draw(object_graph, dirName, vertex_name)

	#print ("dummy",len(g.get_edges([g.edge_index])), len(object_graph.dict_induced),object_graph.dict_induced)

	return len(object_graph.dict_induced)


"""
def main():
	if len (sys.argv) != 2 :
		print ("Usage: python 1.py filename")
		sys.exit (1)

	g = load_graph(sys.argv[1])
	
	graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(2000, 2000), output="two-nodes.png")


	vertex_prop_int = g.new_vertex_property("int",0)	# 0 not induced ------ 1 induced ----- 2 neighbor induced 
	
	object_graph = induced(g, vertex_prop_int)

	

	vertex_checker(object_graph)

	print ("dummy",len(g.get_edges([g.edge_index])), len(object_graph.dict_induced),object_graph.dict_induced)
"""

if __name__ == "__main__":
	main()