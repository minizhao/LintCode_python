#最大假期安排问题

# 思路建一棵多叉树，然后遍历找到最大的结果即可



"""
# 暴力求解，不可行的

class Node(object):
    """docstring for ."""
    def __init__(self,city,week,value,childs=None):
        super(Node, self).__init__()
        self.city = city
        self.week = week
        self.value = value
        self.childs = childs



class Solution:
    """
    @param flights: the airline status from the city i to the city j
    @param days: days[i][j] represents the maximum days you could take vacation in the city i in the week j
    @return: the maximum vacation days you could take during K weeks
    """

    def make_tree(self,flights,days):
        #周数，城市数
        week_nums=len(days[0])
        city_nums=len(days)
        #节点处理队列
        nodes_que=[]
        root=Node(0,-1,0)
        nodes_que.append(root)
        #迭代周数来建造树
        for w in range(week_nums):
            #本次处理的队列节点个数
            nodes_nums=len(nodes_que)
            for _ in range(nodes_nums):
                node_t=nodes_que.pop(0)
                city=node_t.city
                week=node_t.week
                #找到可到达的city
                childs_city=[idx for idx,v in enumerate(flights[city]) if v==1]
                #把现在城市也加入进去
                childs_city.append(city)
                if len(childs_city)>0:
                    node_t.childs=[]
                #处理孩子节点
                for c in childs_city:
                    val=days[c][week+1]
                    child_t=Node(c,week+1,val)
                    node_t.childs.append(child_t)
                    nodes_que.append(child_t)
        return root


    def dfs(self,root,sum_t):

        if root.childs==None:
            return sum_t+root.value
        sum_t+=root.value
        value_arr=[]
        for c in root.childs:
            value_arr.append(self.dfs(c,sum_t))

        return max(value_arr)

    def maxVacationDays(self, flights=[[0,0,0],[0,0,0],[0,0,0]], days=[[1,1,1],[7,7,7],[7,7,7]]):
        tree=self.make_tree(flights,days)
        print(self.dfs(tree,0))




if __name__ == '__main__':
    sol=Solution()
    sol.maxVacationDays()

"""



# 以下是动态规划解法
import copy
class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        week_nums=len(days[0])
        city_nums=len(days)


        #初始化状态，仅仅城市0开放条件
        dp=[0]+[-1]*(city_nums-1)

        # 开始动态规划循环迭代
        for w in range(week_nums):
            next_dp=copy.deepcopy(dp)
            for c,c_value in enumerate(dp):
                if c_value<0:
                    continue
                for c_next in range(city_nums):
                    if c_next==c or flights[c][c_next]==1:
                        next_dp[c_next]=max(next_dp[c_next],c_value+days[c_next][w])

            dp=copy.deepcopy(next_dp)

        return max(dp)
