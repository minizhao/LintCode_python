


#对于问题可以考虑对手的身份转换，如果先手拿了一个或者两个后，后手就会变成先手
# ，这样就容易考虑迭代式．不能让后手变先手后还能赢得游戏 python not 是取反


class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here

        if n<=0:
            return False


        op=[0]
        op.append(True)
        op.append(True)
        for i in range(3,n+1):

            rs=(not op[i-1]) or (not op[i-2])
            op.append(rs)
        return op[n]
