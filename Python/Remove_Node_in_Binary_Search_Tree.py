"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if(root==None or (root.left==None and root.right==None)):
            return None
        dummy=TreeNode(-1)
        dummy.left=root
        parent=self.findTargetParent(dummy,root,value)

        child=None
        if(parent.left!=None and parent.left.val==value):
            child=parent.left
        elif(parent.right!=None and parent.right.val==value):
            child=parent.right
        else:
            return dummy.left

        self.deleteTargetNode(parent,child)
        return dummy.left


    # 查找目标节点
    def findTargetParent(self,parent,node,value):
        if(node==None or node.val==value):
            return parent

        if (value<node.val):
            return self.findTargetParent(node,node.left,value)
        else:
            return self.findTargetParent(node,node.right,value)

    #删除目标节点
    def deleteTargetNode(self,parent,target):
        if(target.right==None):
            if(parent.left==target):
                parent.left=target.left
            else:
                parent.right=target.right
        else:
            replaceNode=target.right
            replaceParent=target
            while(replaceNode.left!=None):
                replaceParent=replaceNode
                replaceNode=replaceNode.left
            if(replaceParent.left==replaceNode):
                replaceParent.left=replaceNode.right
            else:
                replaceParent.right=replaceNode.right

            if(parent.left==target):
                parent.left=replaceNode
            else:
                parent.right=replaceNode

            replaceNode.left=target.left
            replaceNode.right=target.right
