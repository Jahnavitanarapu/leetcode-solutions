'''optimal'''       
class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            current=target-nums[i]
            if current in dict:
                return(dict[current],i)
            dict[nums[i]]=i