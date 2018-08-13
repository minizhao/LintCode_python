"""
链接：https://www.nowcoder.com/practice/cb6c883b123b44399377d0c71e6ba3ea?tpId=8&tqId=11014&rp=1&ru=%2Fta%2Fcracking-the-coding-interview&qru=%2Fta%2Fcracking-the-coding-interview%2Fquestion-ranking&tPage=2
题目描述
对于一棵二叉树，请设计一个算法，创建含有某一深度上所有结点的链表。
给定二叉树的根结点指针TreeNode* root，以及链表上结点的深度，
请返回一个链表ListNode，代表该深度上所有结点的值，请按树上从左往右的顺序链接，
保证深度不超过树的高度，树上结点的值为非负整数且不超过100000。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeLevel:
    def getTreeLevel(self, root, dep):
        queue=[(0,root)]
        L_head=ListNode(0)
        L_head_copy=ListNode(0)
        def level(root,dep):
            while queue:
                lev,node=queue.pop(0)
                if lev==dep:
                    Ln=ListNode(node.val)
                    L_head.next=Ln
                    L_head=Ln
                if node.left == None:
                    queue.append((lev+1,node.left))
                if node.right == None:
                    queue.append((lev+1,node.right))
        return L_head_copy.next



        # write code here
