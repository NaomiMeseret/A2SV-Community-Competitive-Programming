class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_all = defaultdict(int)
        for temp in cpdomains:
            count,domain = temp.split()
            count = int(count)
            subdomain = domain.split('.')
            for i in range(len(subdomain)):
                temp2 = '.'.join(subdomain[i:])
                count_all[temp2] += count
        ans = []
        for domain,count in count_all.items():
            ans.append(str(count)+" " + domain)
        return ans
        