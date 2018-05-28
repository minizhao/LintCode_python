

#查找下一个排列，数组排列是字典顺序的．
# 思路：
# １）先从后往前查找，找到最后的升序点ｋ，即nums[i]<nums[i+1],这个点
# ２）再从后往前找到第一个比nums[k]大的点>big_idx
# ３）交换k和big_idx对应值．
# ４）对[k+1:]后面数组逆序（保证后的部分最小）

class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # write your code here
        if nums==None or len(nums)<=1:
            return nums

        k=-1
        idx=len(nums)-2
        while idx>=0:
            if nums[idx]<nums[idx+1]:
                k=idx
                break
            idx-=1

        if idx==-1:
            nums.reverse()
            return nums

        big_idx=-1
        i=len(nums)-1
        while i>=0:
            if nums[i]>nums[k]:
                big_idx=i
                break
            i-=1


        #交换两个k和big_idx

        tmp=nums[k]
        nums[k]=nums[big_idx]
        nums[big_idx]=tmp

        nums[k+1:]=nums[k+1:][::-1]

        return nums
