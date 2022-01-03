


class Graph:
    
    
    def __init__(self):
        self.adjacency_list = {}


    def print_graph(self):
        for vertices in self.adjacency_list:
            print(vertices, ":" , self.adjacency_list[vertices])


    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False


    def add_edge(self,vertex1,vertex2):
        if vertex2 not in self.adjacency_list[vertex1] and vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        else:
            return False


    def remove_edge(self,vertex1,vertex2):
        if vertex2 in self.adjacency_list[vertex1] and vertex1 in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
        else:
            return False
        

    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            for vertices in self.adjacency_list[vertex]:
                self.adjacency_list[vertices].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('C','B')
#my_graph.remove_edge('A','C')
my_graph.remove_vertex('C')
my_graph.print_graph()