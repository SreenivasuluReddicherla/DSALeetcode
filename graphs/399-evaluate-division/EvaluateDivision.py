class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(curr, target, product, visited):
            if curr == target:
                return product
            visited.add(curr)
            for neighbor, val in graph[curr].items():
                if neighbor not in visited:
                    res = dfs(neighbor, target, product * val, visited)
                    if res != -1:
                        return res
            return -1

        results = []
        for start, end in queries:
            if start not in graph or end not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(start, end, 1, set()))
        return results
        