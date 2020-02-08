import random 
import create_graph as c_g


class RandomGraph() : 


	def __init__(self,nodeNum):        
		self.connected = list()
		self.unconnected = list()
		self.nodes = nodeNum;
		self.fileName = "generate.txt"
		self.random_graph();
		self.generate(0.01);

	def random_graph(self) : 

		self.connected.append(1);
		for  i in range(self.nodes) : 
			self.unconnected.append(i);

	def generate(self,percentage) : 

		extra_edges = (self.nodes * self.nodes * (percentage // 100))

		edges = 0

		allPair = set()

		while len(self.unconnected) != 0 :  
			temp1 = random.randint(0,len(self.connected) - 1) 
			temp2 = random.randint(0,len(self.unconnected) - 1)
			u =self.connected[temp1]
			v = self.unconnected[temp2] 
			allPair.add((u,v))
			self.unconnected.remove(v)
			self.connected.append(v)
			edges += 1


		while extra_edges > 0 :
			temp1 = random.randint(0,len(self.nodes) - 1)
			temp2 = random.randint(0,len(self.nodes) - 1)
			allPair.add((temp1,temp2))
			extra_edges -= 1


		allPairList = list(allPair)
		file = open(self.fileName,"w+")
		for i in range(len(allPair)) : 
			file.write(str(allPairList[i][0]) + "," + str(allPairList[i][1]) + "\n")
		
		file.close()



def genera(vertex):
	g = RandomGraph(vertex)
	c_g.graph_create("generate.txt")

	

