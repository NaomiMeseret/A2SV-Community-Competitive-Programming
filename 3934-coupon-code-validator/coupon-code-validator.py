class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        pat = re.compile(r'^[A-Za-z0-9_]+$')   
        group = {x: [] for x in order}
        for c, l, a in zip(code, businessLine, isActive):
            if not a:
                continue
            if not c:
                continue
            if l not in group:
                continue
            if not pat.match(c):
                continue
            group[l].append(c)
        out = []
        for x in order:
            out.extend(sorted(group[x]))
        return out


                