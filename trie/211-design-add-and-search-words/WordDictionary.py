class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)

    def _dfs(self, node, word, i):
        if not node:
            return False
        if i == len(word):
            return node.is_end

        ch = word[i]
        if ch == '.':
            for child in node.children:
                if child and self._dfs(child, word, i + 1):
                    return True
            return False
        else:
            return self._dfs(node.children[ord(ch) - ord('a')], word, i + 1)