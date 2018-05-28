import heapq
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """


    def kthSmallest(self,matrix,k):
        my_heapq=[matrix[0][0]]
        x_y_sum=0
        count=0

        x_max=(len(matrix)-1)
        y_max=(len(matrix[0])-1)
        x_y_sum_max=x_max+y_max

        while True:

            if x_y_sum<=x_y_sum_max and x_y_sum>0:
                for x in range(x_y_sum+1):
                    if x<=x_max and x_y_sum<=(y_max+x):
                        heapq.heappush(my_heapq,matrix[x][x_y_sum-x])

            for _ in range(1):
                min_val=heapq.heappop(my_heapq)
                count+=1
                if count==k:
                    return min_val
            x_y_sum+=1



if __name__ == '__main__':
    matrix=[[1],[2],[3],[100],[101],[1000],[9999]]
    sol=Solution()
    rst=sol.kthSmallest(matrix,5)
    print(rst)
