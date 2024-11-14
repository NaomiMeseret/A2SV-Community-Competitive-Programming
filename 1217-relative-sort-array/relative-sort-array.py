class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        maximum=max(arr1)
        count=[0]*(maximum+1)
        for num in arr1:
            count[num]+=1
        sorted_arr=[]
        for num in arr2:
            if count[num]>0:
                sorted_arr.extend([num]*count[num])
                count[num]=0
        for num in range(maximum+1):
            if count[num]>0:
                sorted_arr.extend([num]*count[num])
        return sorted_arr
