class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
class WordDictionary:

    def __init__(self):
       self.root = TrieNode()  

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True
    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
            ch = word[idx]
            if ch == ".":
                for child in node.children:
                    if child is not None and dfs(child , idx+1):
                        return True
                return False
            else:
                i = ord(ch)-ord("a")
                child = node.children[i]
                if child is None:
                    return False
                return dfs(child , idx+1)
        
        return dfs(self.root , 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)