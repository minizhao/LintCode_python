"""

链接：https://www.nowcoder.com/practice/dc943274e8254a9eb074298fb2084703?tpId=85&tqId=29894&tPage=1&rp=1&ru=/ta/2017test&qru=/ta/2017test/question-ranking
题目描述
春天是鲜花的季节，水仙花就是其中最迷人的代表，数学上有个水仙花数，他是这样定义的： “水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，比如：153=1^3+5^3+3^3。 现在要求输出所有在m和n范围内的水仙花数。
输入描述:
输入数据有多组，每组占一行，包括两个整数m和n（100 ≤ m ≤ n ≤ 999）。
输出描述:
对于每个测试实例，要求输出所有在给定范围内的水仙花数，就是说，输出的水仙花数必须大于等于m,并且小于等于n，如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开;
如果给定的范围内不存在水仙花数，则输出no;
每个测试实例的输出占一行。
示例1
输入

复制
100 120
300 380
输出

复制
no
370 371

思路:遍历范围中的每一个数字
"""



import sys
line=sys.stdin.readline().split()
nums=[int(x) for x in line]
num1,num2=nums[0],nums[1]
res=[]
for x in range(num1,num2):
    c=0
    for n in list(str(x)):
        c+=int(n)**3
    if x==c:
        res.append(x)
if len(res)==0:
    print("no")
else:
    print(' '.join([str(x) for x in res]))
