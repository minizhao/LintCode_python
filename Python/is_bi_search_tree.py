"""
链接：https://www.nowcoder.com/practice/536c0199151245f897da2c5390930657?tpId=8&tqId=11015&rp=1&ru=%2Fta%2Fcracking-the-coding-interview&qru=%2Fta%2Fcracking-the-coding-interview%2Fquestion-ranking&tPage=2
题目描述
请实现一个函数，检查一棵二叉树是否为二叉查找树。
给定树的根结点指针TreeNode* root，请返回一个bool，代表该树是否为二叉查找树。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Checker:

    def checkBST(self, root):
        nums=[]
        def ts(node):
            if node == None:
                return
            ts(node.left)
            nums.append(node.val)
            ts(node.right)

        ts(root)
        if sorted(nums)==nums:
            return True
        else:
            return False
