import copy
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    #从顺序数组中删除重复元素
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        count=0
        current_num=None
        dum=copy.deepcopy(nums)
        #设定一个起始索引，开始遍历，符合条件的往前复制给原来数组
        rst_idx=0
        for idx,item in enumerate(dum):
            if item==current_num:
                count+=1
                if count<=2:
                    nums[rst_idx]=item
                    rst_idx+= 1
            else:
                current_num=item
                count=1
                nums[rst_idx]=item
                rst_idx+= 1

        return rst_idx
