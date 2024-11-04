class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        # my_dict = {"content":[path]}

        
        for path in paths:
            dirr,*files =  path.split()

            for f in files:
                fname,fcont = f.split('(')
                my_dict[fcont].append(dirr + '/' + fname)
        ans=[]
        for value in my_dict.values():
            if len(value)>1:
                ans.append(value)
        return ans
        