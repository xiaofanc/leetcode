class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Topological Sorting - look for all the centroid nodes in a tree
        BFS - trim out the leaf nodes layer by layer until we reach the core of the graph, 1 or 2 nodes left with same height
        """
        # base case
        if n <= 2:
            return [i for i in range(n)]
        
        # Build the graph with the adjacency list
        # Time: O(|V|-1)  Space: O(|V|+|V|-1)
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        # initialize the first layer of the leaves
        # Time: O(|V|) 
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
                
        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves and edges from the leaves - BFS
            # Time: O(|V|+|V|-1) Space: worst O(|V|-1)
            while leaves:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
        
        return leaves

if __name__ == '__main__':
    s - Solution()
    print(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))    # [1]    



      
        
        
