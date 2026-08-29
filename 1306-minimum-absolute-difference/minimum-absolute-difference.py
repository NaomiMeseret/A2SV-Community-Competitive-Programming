class Solution(object):
    def minimumAbsDifference(self, arr):
        new_arr=sorted(arr)
        my_dict={}
        for i in range(len(new_arr)-1):
            diff=new_arr[i+1]-new_arr[i]
            if diff in my_dict:
                my_dict[diff].append([new_arr[i],new_arr[i+1]])
            else:
                my_dict[diff]=[[new_arr[i],new_arr[i+1]]]
        result=min(my_dict.keys())
        return my_dict[result]
        
        
        


      
        