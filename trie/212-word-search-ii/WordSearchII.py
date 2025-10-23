class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        root = self.build_trie(words)
        res = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, res)
        return res

    def build_trie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        return root

    def dfs(self, board, i, j, node, res):
        ch = board[i][j]
        if ch == '#' or ch not in node.children:
            return
        node = node.children[ch]
        if node.word:
            res.append(node.word)
            node.word = None  # prevent duplicates

        board[i][j] = '#'
        for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = i + x, j + y
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                self.dfs(board, nx, ny, node, res)
        board[i][j] = ch