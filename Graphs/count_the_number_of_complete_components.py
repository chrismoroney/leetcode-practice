"""
Count the Number of Complete Components

You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. 
You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.
"""

from collections import defaultdict

class Solution(object):
    def count_complete_components(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        count = 0
        visited = set()

        def dfs(node, info):
            visited.add(node)
            info[0] += 1
            info[1] += len(graph[node])

            for vertex in graph[node]:
                if vertex not in visited:
                    dfs(vertex, info)

        for v in range(n):
            if v in visited:
                continue
        
            info = [0, 0]
            dfs(v, info)

            if info[0] * (info[0] - 1) == info[1]:
                count += 1

        return count
    
if __name__ == "__main__":
    sol = Solution()
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]

    print(sol.count_complete_components(n, edges))

