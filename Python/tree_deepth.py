

"""
题目链接：https://www.nowcoder.com/practice/4faa2d4849fa4627aa6d32a2e50b5b25?tpId=85&&tqId=29897&rp=1&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
现在有一棵合法的二叉树，树的节点都是用数字表示，现在给定这棵树上所有的父子关系，求这棵树的高度
输入描述:
输入的第一行表示节点的个数n（1 ≤ n ≤ 1000，节点的编号为0到n-1）组成，
下面是n-1行，每行有两个整数，第一个数表示父节点的编号，第二个数表示子节点的编号
输出描述:
输出树的高度，为一个整数
示例1
输入

5
0 1
0 2
1 3
1 4


输出

3

思路：每个节点计算其层数，最后选择最大的层数加1
"""

import sys
n=int(sys.stdin.readline().strip())
max_deepth=1
data={0:1}
node_childs_num={0:0}
for _ in range(n-1):
    line= sys.stdin.readline().strip().split()
    nums=[int(x) for x in line]
    parent,child=nums[0],nums[1]
    if parent not in data.keys():
        continue
    parent_deepth=data.get(parent)
    node_cn=node_childs_num.get(parent,0)
    if node_cn>=2:
        continue
    data[child]=parent_deepth+1
    node_childs_num[parent]=node_childs_num.get(parent,0)+1
    if parent_deepth+1>max_deepth:
        max_deepth=parent_deepth+1
print(max_deepth)
