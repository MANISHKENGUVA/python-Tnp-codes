 
from collections import defaultdict 


graph = defaultdict(list) 
def addEdge(graph,u,v): 
	graph[u].append(v) 


def generate_edges(graph): 
	edges = [] 


	for node in graph: 
		
	
		for neighbour in graph[node]: 
			
			
			edges.append((node, neighbour)) 
	return edges 

# declaration of graph as dictionary 
addEdge(graph,'a','c') 
addEdge(graph,'b','c') 
addEdge(graph,'b','e') 
addEdge(graph,'c','d') 
addEdge(graph,'c','e') 
addEdge(graph,'c','a') 
addEdge(graph,'c','b') 
addEdge(graph,'e','b') 
addEdge(graph,'d','c') 
addEdge(graph,'e','c') 


print(generate_edges(graph)) 


#Bfs Implementaion 
vis = []
q = []

for node in graph:
    if node not in vis:
        q.append(node)
        vis.append(node)

    while q:
        current_node = q.pop(0)

        for child in graph[current_node]:
            if child not in vis:
                q.append(child)
                vis.append(child)#in order not to in loop rereapeting occur elements 
                
                
print(vis)

        
    






