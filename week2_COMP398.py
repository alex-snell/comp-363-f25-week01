
class MST:
    #for an undirected, weighted graph
    def min_span_tree(G):
        #initilize
        INF = float('inf')
        n = len(G)
        T = [[INF for _ in range(n)] for _ in range(n)]
        # store 0 distance for same vertex (0,0) (1,1)...
        for i in range(n):
          T[i][i] = 0
          #more than one component
        more_components = True
        while more_components:
            # count and label components
            num_components, component_labels = MST.count_and_label(T)
            
            # if only 1 component remains, set to false
            if num_components <= 1:
                more_components = False
            # find safe edge between components
            safe_edge = MST.find_safe_edge(G, component_labels, num_components)
            
            if safe_edge is None:
                more_components = False  # no more edges to add (disconnected graph)
            
            if more_components:
                # connect two components with the safe edge
                u, v, weight = safe_edge
                T[u][v] = weight
                T[v][u] = weight  # undirected graph these values should be the same
        
        return T #where t is the adj list
    def find_safe_edge(G, component_labels, num_components):     
       # find the minimum weight edge that connects two different components
        n = len(G)
        INF = float('inf')
        min_edge = None
        min_weight = INF
        
        # examine all edges in the original graph G
        for u in range(n):
            for v in range(u + 1, n): 
                if G[u][v] != INF and G[u][v] != 0:  #check for valid edge
                    # check if u and v are in different components
                    if component_labels[u] != component_labels[v]:
                        if G[u][v] < min_weight:
                            min_weight = G[u][v]
                            min_edge = (u, v, G[u][v])
        
        return min_edge
    
    def reachability_of(s:int, G) -> list[int]:
        local_infinity = float('inf')
        reach = [] # return object
        bag = [s] # a place to store which vertex to process next

        while bag: #best way to test if empty len(bag) > 0, style in python can be while bag:
            v = bag.pop()
            if v not in reach:
                reach.append(v)
                #add v's neighbors to the bag, go to corresponding row/column in adj matrix
                for u in range(len(G)):
                    if G[v][u] != local_infinity:
                        bag.append(u)
        return reach
    
    def count_and_label(graph):
      #shortcut to number of verticies
      n = len(graph)
      #track verticies visited
      visited = []
      # count components
      count = 0
      #track component labels
      comp_labels = [None] * n
      #consider every vertex in the graph
      for u in range(n):
        #have we seen value at index u before
        if u not in visited:
          #new component
          count += 1
          #find all verticies reachable from u
          reachable_from_u = MST.reachability_of(u, graph)  
          #label verticies
          for vertex in reachable_from_u:
            comp_labels[vertex] = count
          #mark all visited
          visited.extend(reachable_from_u)
      #done return count and component
      return count, comp_labels
    
