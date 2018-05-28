

class Solution:
    """
    @param Maze: 
    @return: nothing
    """


    def is_in_Maze(self,m,position):
        if 0<=position[0]<len(m) and position[0]<len(m) and 0<=position[1] and position[1]<len(m[0]) and m[position[0]][position[1]]!=-1:
            return True

    def get_childs(self,m,s_position):
        childs=[]
        s_position=[int(x) for x in s_position.split(',')]

        if self.is_in_Maze(m,[s_position[0],s_position[1]-1]):
            childs.append([str(s_position[0])+','+str(s_position[1]-1),m[s_position[0]][s_position[1]-1]])
            m[s_position[0]][s_position[1]-1]=-1

        if self.is_in_Maze(m,[s_position[0]-1,s_position[1]]):
            childs.append([str(s_position[0]-1)+','+str(s_position[1]),m[s_position[0]-1][s_position[1]]])
            m[s_position[0]-1][s_position[1]]=-1

        if self.is_in_Maze(m,[s_position[0],s_position[1]+1]):
            childs.append([str(s_position[0])+','+str(s_position[1]+1),m[s_position[0]][s_position[1]+1]])
            m[s_position[0]][s_position[1]+1]=-1

        if self.is_in_Maze(m,[s_position[0]+1,s_position[1]]):
            childs.append([str(s_position[0]+1)+','+str(s_position[1]),m[s_position[0]+1][s_position[1]]])
            m[s_position[0]+1][s_position[1]]=-1
        return childs

    def make_tree(self,m,s_position):
        tree={}
        que=[s_position]
        while True:
            if len(que)==0:
                break
            crrent_point=que[0]

            que.remove(crrent_point)
            childs=self.get_childs(m,crrent_point)
            que=que+[x[0] for x in childs if x[1]!='#'] 
            if len(childs)>0:
                tree[crrent_point]=childs

        return tree

    def find_best_path(self,tree,point,sum):

        p_idx=point[0]
        p_type=point[1]

        if p_type=='E':
            return sum

        if p_type=='#' or p_idx not in tree.keys():
            return float('inf')

        sum=sum+1
        childs=tree[p_idx]

        sum_list=[]

        for c in childs:
            sum_list.append(self.find_best_path(tree,c,sum))

        return min(sum_list)

    def Portal(self, Maze):

        Maze=[list(tuple(x)) for x in Maze]
        print(Maze)
        s_position=''
        for i in range(len(Maze)):
               if 'S' in Maze[i]:
                s_position=str(i)+','+str(Maze[i].index('S'))
                Maze[i][Maze[i].index('S')]=-1
                break
        print(s_position)
        tree=self.make_tree(Maze,s_position)
        print(tree)
        rst=self.find_best_path(tree,[s_position,'S'],0)

        if (rst==float('inf')):
            return -1
        return rst




if __name__ == '__main__':
    m=["S*E","***","#**","##E"]

    sol=Solution()
    print(sol.Portal(m))
    