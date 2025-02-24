class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Build the undirected graph.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Compute Bob's path from 'bob' to 0 using BFS.
        parent = {bob: None}
        queue = deque([bob])
        while queue:
            node = queue.popleft()
            if node == 0:
                break
            for nei in graph[node]:
                if nei not in parent:
                    parent[nei] = node
                    queue.append(nei)
        
        # Reconstruct Bob's path from 0 to bob.
        bob_path = []
        node = 0
        while node is not None:
            bob_path.append(node)
            node = parent.get(node)
        bob_path.reverse()
        # Create a mapping: node -> time (or index) on Bob's path.
        bob_time = {node: t for t, node in enumerate(bob_path)}
        
        # BFS for Alice's path starting from node 0.
        max_income = float('-inf')
        queue = deque([(0, 0, 0)])  # (node, time, current_income)
        visited = {0}  # Use a set for O(1) lookups.
        while queue:
            node, t, income = queue.popleft()
            
            # Update income based on when Bob reaches the node.
            if node not in bob_time or t < bob_time[node]:
                income += amount[node]
            elif t == bob_time[node]:
                income += amount[node] // 2
            
            # If it's a leaf (and not the root), update max_income.
            if node != 0 and len(graph[node]) == 1:
                max_income = max(max_income, income)
            
            # Traverse adjacent nodes.
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, t + 1, income))
        
        return max_income