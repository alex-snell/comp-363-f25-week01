
class mst():
    G = [
        [0,1,1,0],
        [1,0,0,1],
        [1,0,0,1],
        [0,1,1,0],
                ]
    marked = 0
    comp = {}
    count = 0
    F = 0
    def __init__(self, new_g):
        self.G = new_g
        self.marked = set()
        self.comp = {}
        self.count = 0
        self.F = 0

    

    def count_label(self):
       
        for v in range(len(self.F)):
            if v not in self.marked:
                self.count+=1
                self.marked.add(v)
                self.label_one(v)
        

    def label_one(self, v):
        bag = []
        bag.append(v)
        self.marked.add(v)
        self.comp[v] = self.count
        while bag:
            vertex = bag.pop()
            for w in range(len(self.F)):
                if self.F[vertex][w] == 1 and vertex not in self.marked:
                    self.marked.add(w)
                    self.comp[w] = self.count
                    bag.append(w)
        

    def get_edge(self):
        edges = []
        for i in range(len(self.F)):
            for j in range(i+1, len(self.F)):
                if self.F[i][j] == 1:
                    edges.append((i,j))
        return edges

    def safe_edge(self, F, comp):
        is_safe_edge = False
        for i in range(len(F)):
            for j in range(i+1, len(F)):
                if self.G[i][j]== 1 and F[i][j] == 0 and comp[i] != comp[j]:
                    F[i][j] = 1
                    F[j][i] = 1
                    is_safe_edge = True
                    return is_safe_edge
        return is_safe_edge

    def build_mst(self):
        F = [[0] * len(self.G) for _ in range(len(self.G))]
        self.set_F(F)
        self.count_label()
        count = self.count
        while count > 1:
            if self.safe_edge(F,self.comp):
        
                self.marked = set()
                self.comp = {}
                self.count = 0
                self.count_label()
                count = self.count
            else:
                count = 1
        return F
    
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