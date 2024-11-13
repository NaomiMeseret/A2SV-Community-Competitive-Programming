class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size=len(heights)
        for i in range(size):
            max_index=i
            for j in range(i+1,size):
                if heights[j]>heights[max_index]:
                    max_index=j
            heights[max_index],heights[i]=heights[i],heights[max_index]
            names[max_index],names[i]=names[i],names[max_index]
        return names
        
        