class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = {}
        for a in allowed:
            key = a[0] + a[1]
            if key not in mp:
                mp[key] = []
            mp[key].append(a[2])
        def dfs(row):
            if len(row) == 1:
                return True
            
            def build(i, cur):
                if i == len(row) - 1:
                    return dfs(cur)
                
                pair = row[i] + row[i+1]
                if pair not in mp:
                    return False
                
                for ch in mp[pair]:
                    if build(i + 1, cur + ch):
                        return True
                return False
            
            return build(0, "")
        return dfs(bottom)