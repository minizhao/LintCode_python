#动态规划问题，如果dp[i] 代表第i个的可能情况．如果其和第i-1个颜色不相同的话，有dp[i-1]*(k-1)中
# 如果第i－１个相同的话，要保证i-1和i-2必须不同．所以有dp[i-2]*(k-1)种情况，这样动态规划求解即可

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        dp=[0,k]
        dp.append(k+k*(k-1))
        print(dp)
        for i in range(3,n+1):
            dp.append((k-1)*(dp[i-1]+dp[i-2]))
        print(dp)
        return dp[n]
