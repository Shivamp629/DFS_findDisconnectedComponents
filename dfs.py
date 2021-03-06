from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
  
  def addEdge(self,v1,v2):
    self.graph[v1].append(v2)
  
  def DFS(self, start):
    visitedSet = set()
    countGraphs = 0
    components = []
    for neighbor in self.graph.keys():
      verticesInComponent = []
      if (neighbor not in visitedSet):
        self.DFSHelper(neighbor, visitedSet, verticesInComponent)
        components.append(verticesInComponent)
        countGraphs += 1
    outputText = ("Graph has {} components and the components each contain the following values {}").format(countGraphs, components)
    print(outputText)

  def DFSHelper(self, node, visitedSet, verticesInComponent):
    visitedSet.add(node)
    verticesInComponent.append(node)
    for neighbor in self.graph.get(node):
      if (neighbor not in visitedSet):
        self.DFSHelper(neighbor, visitedSet, verticesInComponent)

  
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.addEdge(5,5)
  
print ("Following is Depth First Traversal")
g.DFS(0) 
