from graph_tool.all import *
import sys
import numpy as np
from graph_tool import Graph
import os


class induced:
	def __init__(self, graph, vertex_name):
		self.graph = graph
		self.vertex_prop_int = self.graph.new_vertex_property("int",0)			# 0 not induced ------ 1 induced ----- 2 neighbor induced 
		self.dict_induced = {}
		self.dict_induced_real_name = {}
		self.vertex_name = vertex_name
		self.sorted_vertex_array =  self.sort_with_zip()

		self.vertex_color = graph.new_vertex_property("string")
		self.edge_color = graph.new_edge_property("string")

		for r in graph.vertices():
			self.vertex_color[r] = "#C133FF"

		arr = []

		for r in graph.edges():
			self.edge_color[r] = "#C133FF"
			arr.append(r)


	def sort_with_zip(self):

		vers = self.graph.get_vertices()

		arr = [0] * len(vers)

		for i in range(len(vers)):
			arr[i] = len(self.graph.get_all_edges(vers[i], [self.graph.edge_index]))

		a,v = zip(*sorted(zip(arr,vers)))

		return v


def vertex_checker(object_graph, index):
	

	if object_graph.vertex_prop_int[object_graph.sorted_vertex_array[index]] == 0:
		edge_checker(object_graph.sorted_vertex_array[index], object_graph)

	if index != len(object_graph.sorted_vertex_array) - 1:
		vertex_checker(object_graph, index + 1)
	

def min_edge(object_graph,edges):
	
	dict = {}
	
	for vertex in edges:
		if object_graph.vertex_prop_int[vertex[1]] == 0:
			dict[vertex[1]] = len(object_graph.graph.get_all_edges(vertex[1], [object_graph.graph.edge_index]))
	
	return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}


def edge_checker(vertex, object_graph):
	
	edges = object_graph.graph.get_all_edges(vertex, [object_graph.graph.edge_index])

	sorted_edges = min_edge(object_graph,edges)


	for i in sorted_edges:
		if object_graph.vertex_prop_int[i] == 0:
			object_graph.dict_induced[vertex] = i
			object_graph.dict_induced_real_name[object_graph.vertex_name[vertex]] = object_graph.vertex_name[i]
			change_prop_int(vertex, i, sorted_edges, object_graph)
			break
	
		


def change_prop_int(vertex, edge, edges, object_graph):
	
	object_graph.vertex_prop_int[vertex] = 1			#vertexleri induced yapma
	object_graph.vertex_prop_int[edge] = 1


	object_graph.vertex_color[vertex] = "#5EFF33" 
	object_graph.vertex_color[edge] = "#5EFF33"
															#vertexlere renk atama
	for a in object_graph.graph.edges():
		b = list(a)
		if b[0] == vertex and b[1] == edge or b[1] == vertex and b[0] == edge:
			object_graph.edge_color[a] = "#5EFF33"


			################3 silinebilir  ##############################3
	#result = np.where(object_graph.sorted_vertex_array == edge)

	#object_graph.sorted_vertex_array = np.delete(object_graph.sorted_vertex_array, result[0][0], 0)
		###############################################################################

	for i in edges:
		if object_graph.vertex_prop_int[i] == 0:				#vertexin edgelerine 
			object_graph.vertex_prop_int[i] = 2


	temp = object_graph.graph.get_all_edges(edge, [object_graph.graph.edge_index])

	for i in temp:
		if object_graph.vertex_prop_int[i[1]] == 0:
			object_graph.vertex_prop_int[i[1]] = 2


	

def start(g, name, dirName):
	

	vertex_name = g.new_vertex_property("string")


	i = 0
	
	for r in g.vertices():
		vertex_name[r] = name[i]
		i += 1
	
	
	object_graph = induced(g, vertex_name)

	vertex_checker(object_graph, 0)

	#print ("induced", len(object_graph.dict_induced),object_graph.dict_induced_real_name)

	write_to_file_and_draw(object_graph, dirName, vertex_name)


	return len(object_graph.dict_induced)


def write_to_file_and_draw(object_graph, dirName, vertex_name):

	if not os.path.exists(dirName + "/Heuristic"):
		os.mkdir(dirName + "/Heuristic")

	graph_draw(object_graph.graph, vertex_fill_color = object_graph.vertex_color, vertex_font_size=15, output_size=(800, 800),  edge_color = object_graph.edge_color, vertex_text = vertex_name, output=dirName + "/Heuristic/graph.png")	

	
	f = open(dirName + "/Heuristic/matchs.txt", "w")

	f.write("Induced Match Number  :  ")
	f.write(str(len(object_graph.dict_induced)))
	f.write("\n\nMatches:\n\n")

	for i in object_graph.dict_induced_real_name.keys():
		f.write(i)
		f.write(", ")
		f.write(object_graph.dict_induced_real_name[i])
		f.write("\n")
	f.close()

	graph_draw(object_graph.graph, vertex_fill_color = object_graph.vertex_color, vertex_font_size=15, output_size=(800, 800),  edge_color = object_graph.edge_color, vertex_text = vertex_name)#, output=dirName + "/Heuristic/graph.png")


def main():
	print (sys.argv)
	if len (sys.argv) != 2 :
		print ("Usage: python 1.py filename")
		sys.exit (1)

	g = load_graph(sys.argv[1])

	start(g,[])


if __name__ == "__main__":

	main()

