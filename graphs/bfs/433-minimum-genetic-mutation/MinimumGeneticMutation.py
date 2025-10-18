class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        queue = deque([(start, 0)])
        visited = {start}
        genes = ['A', 'C', 'G', 'T']

        while queue:
            gene, steps = queue.popleft()
            if gene == end:
                return steps

            for i in range(len(gene)):
                for g in genes:
                    mutated = gene[:i] + g + gene[i+1:]
                    if mutated in bank and mutated not in visited:
                        visited.add(mutated)
                        queue.append((mutated, steps + 1))
        return -1

        