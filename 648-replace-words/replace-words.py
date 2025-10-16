class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()    
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True
    def find_shortest_root(self , word:str):
        curr = self.root
        prefixChars = []
        for ch in word:
            idx = ord(ch) - ord("a")
            if curr.children[idx] is None:
                return None
            curr = curr.children[idx]
            prefixChars.append(ch)
            if curr.is_end:
                return "".join(prefixChars)
        return None
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie. insert(root)
        parts = sentence.split()
        for i , w in enumerate(parts):
            r = trie.find_shortest_root(w)
            if r is not None:
                parts[i] = r
        return " ".join(parts)


        