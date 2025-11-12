
class mst():
    G = [
        [0,1,1,0],
        [1,0,0,1],
        [1,0,0,1],
        [0,1,1,0],
                ]
    #marked/visted
    marked = 0
    #components
    comp = {}
    #number of components
    count = 0
    #copy
    F = 0

    def __init__(self, new_g):
        self.G = new_g
        self.marked = set()
        self.comp = {}
        self.count = 0
        self.F = 0

    

    def count_label(self):
       #go through copy
        for v in range(len(self.F)):
            #if not vertex not in marked
            if v not in self.marked:
                #add num componets
                self.count+=1
                #add vertex number
                self.marked.add(v)
                #continue
                self.label_one(v)
        

    def label_one(self, v):
        #bag to process vertices
        bag = []
        #add v to bag
        bag.append(v)
        #add v to marked 
        self.marked.add(v)
        #in components list add number of components to components list at v
        self.comp[v] = self.count
        while bag:
            #take vertex from bag
            vertex = bag.pop()
            #for length of copy
            for w in range(len(self.F)):
                #check if the F[vertex][w] is a valid edge (==1)
                #check that vertex is not marked/visted
                if self.F[vertex][w] == 1 and vertex not in self.marked:
                    #add w to marked and to bag
                    self.marked.add(w)
                    self.comp[w] = self.count
                    bag.append(w)
        

    def get_edge(self):
        #create a new edges list
        edges = []
        for i in range(len(self.F)):
            for j in range(i+1, len(self.F)):
                if self.F[i][j] == 1:
                    edges.append((i,j))
        return edges

    def safe_edge(self):
        is_safe_edge = False
        for i in range(len(self.F)):
            for j in range(i+1, len(self.F)):
                #check if there is an edge in original graph G, and if its not yet in our spanning tree
                #also checks that numCompents at index i does not match the num compents at index j
                if self.G[i][j]== 1 and self.F[i][j] == 0 and self.comp[i] != self.comp[j]:
                    #sets both edges i,j and j,i to 1 in the spanning tree
                    self.F[i][j] = 1
                    self.F[j][i] = 1
                    #sets safe edge to true and returns
                    is_safe_edge = True
                    return is_safe_edge
        return is_safe_edge

    def build_mst(self):
        #create copy
        F = [[0] * len(self.G) for _ in range(len(self.G))]
        #set class value
        self.set_F(F)
        #call count and label
        self.count_label()
        #count edges added
        edges_added = 0
        n = len(self.G)
        while edges_added < n-1:
            #check for safe edge
            if self.safe_edge():
                edges_added += 1
                #if there is reset all values
                self.marked = set()
                self.comp = {}
                self.count = 0
                self.count_label()
                
            else:
                #if not a safe edge break loop by setting edges_added to n -1
                edges_added = n -1
            #return spanning tree
        return F
    #helper methods
    def set_F(self, F):
        self.F = F
    def num_components(self):
        return self.count
    def get_comp(self):
        return self.comp
    
def main():
    G = [
        [0,1,1,0],
        [1,0,0,1],
        [1,0,0,1],
        [0,1,1,0],
                ]
    print("Original graph G:")

    for row in G:
        print(row)
    tree = mst(G)
    F = tree.build_mst()

    print("\nSpanning tree F:")
    for row in F:
        print(row)


    print(f"\nNumber of components in F: {tree.num_components()}")
    print(f"Component assignments: {tree.get_comp()}")

if __name__ == "__main__":
    main()
