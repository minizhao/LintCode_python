
"""
题目：https://www.nowcoder.com/practice/74acf832651e45bd9e059c59bc6e1cbf?tpId=85&&tqId=29892&rp=1&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
一只袋鼠要从河这边跳到河对岸，河很宽，但是河中间打了很多桩子，每隔一米就有一个，每个桩子上都有一个弹簧，、
袋鼠跳到弹簧上就可以跳的更远。每个弹簧力量不同，用一个数字代表它的力量，如果弹簧力量为5，、
就代表袋鼠下一跳最多能够跳5米，如果为0，就会陷进去无法继续跳跃。河流一共N米宽，袋鼠初始位置就在第一个弹簧上面，、
要跳到最后一个弹簧之后就算过河了，给定每个弹簧的力量，求袋鼠最少需要多少跳能够到达对岸。如果无法到达输出-1
输入描述:
输入分两行，第一行是数组长度N (1 ≤ N ≤ 10000)，第二行是每一项的值，用空格分隔。
输出描述:
输出最少的跳数，无法到达输出-1
示例1
输入

复制
5
2 0 1 1 1
输出

复制
4
"""


"""
#多叉树分治算法，超时
import sys
class Tree(object):
    def __init__(self,value,idx=0,childs=[]):
        super(Tree, self).__init__()
        self.value = value
        self.idx=idx
        self.childs = childs

def make_tree(power_list):
    queue=[]
    T=Tree(power_list[0],0)
    queue.append(T)
    while queue:
        node=queue.pop(0)
        v,idx=node.value,node.idx
        for i in range(1,v+1):
            if idx+i >len(power_list)-1:
                continue
            t=Tree(value=power_list[idx+i],idx=idx+i,childs=[])
            node.childs.append(t)
            queue.append(t)
    return T

def dfs(node,sum):
    if node.value==0:
        return float("inf")
    if node.childs==[]:
        return sum+1
    sum=sum+1
    childs=node.childs
    sum_list=[]
    for node in childs:
        sum_list.append(dfs(node,sum))
    return min(sum_list)

N=sys.stdin.readline()
line=sys.stdin.readline().strip()
power_list=[int(x) for x in line.split()]
T=make_tree(power_list)
steps=dfs(T,0)
print(steps)
"""


"""
动态规划算法:通过
"""

import sys
# N=int(sys.stdin.readline())
# line=sys.stdin.readline().strip()
N=5
line="2 0 1 1 1"
power_list=[int(x) for x in line.split()]
dp=[(0,power_list[0],0)]+[-1]*(N-1)
steps=[]

while dp:
    cpile=dp.pop(0)
    if cpile==-1:
        continue
    step,value,idx=cpile
    for i in range(value):
        if i>len(dp)-1:
            continue
        if dp[i]==-1:
            dp[i]=(step+1,power_list[idx+i+1],idx+i+1)
            if idx+i+1+power_list[idx+i+1]>N-1:
                steps.append(step+1+1)
            if idx+i+1==N-1:
                steps.append(step+1+1)
        else:
            if step+1<dp[i][0]:
                dp[i]=(step+1,dp[i][1],dp[i][2])
                if idx+i+1+dp[i][1]>N-1:
                    steps.append(step+1+1)
                if idx+i+1==N-1:
                    steps.append(step+1+1)
if len(steps)==0:
    print(-1)
else:
    print(min(steps))
