class TrieNode:
    def __init__(self):
        self.children = {}
        self.total  = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.old_vals  = {}
    def insert(self, key: str, val: int) -> None:
        delta = val-self.old_vals.get(key,0)
        self.old_vals[key] = val
        node = self.root
        node.total+=delta
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.total += delta
    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.total
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)