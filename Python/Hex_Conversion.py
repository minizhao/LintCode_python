class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """

    #ｋ进制的转换，除看k取整法
    def hexConversion(self, n, k):
        if n==0:
            return '0'
        code_list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        cov_nums=[]
        while n!=0:
            cov_num=n%k
            cov_nums.insert(0,cov_num)
            n=n//k

        rst=''.join(code_list[x] for x in cov_nums)
        return rst
