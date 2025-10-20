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
    def is_valid_word(self , word:str):
        curr = self.root
        for i  , char in enumerate(word):
            idx =ord(char) - ord("a")
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
            if i<len(word) - 1 and not curr.is_end:
                return False
        return curr.is_end   
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w)
        res = ""
        for w in words:
            if trie.is_valid_word(w):
                if len(w)>len(res)or (len(w)==len(res) and w<res):
                    res = w
        return res
        