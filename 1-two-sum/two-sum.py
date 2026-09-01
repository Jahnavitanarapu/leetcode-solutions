'''brute force'''
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                target==nums[i]+nums[j]
        return(i,j)        


'''optimal solution'''
class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            current_element=target-nums[i]
            if current_element in dict:
                return(dict[current_element],i)
            dict[nums[i]]=i    


