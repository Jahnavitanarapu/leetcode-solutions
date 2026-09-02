class Solution(object):
    def rotate(self, nums, k):
       n=len(nums)
       k=k%n
       nums.reverse()
       nums[:k]=reversed(nums[:k])
       nums[k:]=reversed(nums[k:])
       return nums

'''class Solution(object):
    def rotate(self, nums, k):
       for i in range(k):
        last=nums[-1]
       for i in range(len(nums)-1,0,-1):
        nums[i]=nums[i-1]
       nums[0]=last
       return nums '''


