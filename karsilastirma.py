
import create_graph as cg
import os


def main():


	dosyalar = os.listdir("/home/nurullah/Desktop/bitirme/project/100vertex_degree7")
	
	dosya = open("result.txt","w")
	
	
	dosya.write("Vertex\tEdge\tHeursitic\tGreedy\t\n")

	for i in dosyalar:
		#print (i)
		l_heuristic, l_greedy, vertex, edges = cg.graph_create("/home/nurullah/Desktop/bitirme/project/100vertex_degree7/" + i)
		temp = str(vertex) + "\t" + str(edges) + "\t" + str(l_heuristic) + "\t" + str(l_greedy) + "\n"
		#print (temp)
		dosya.write(temp)
		#break


	dosya.close()









if __name__ == '__main__':
	main()