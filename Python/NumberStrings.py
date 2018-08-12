"""
题目描述
设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
输入描述:
有多组测试样例，每组测试样例包含两行，第一行为一个整数N（N<=100），第二行包含N个数(每个数不超过1000，空格分开)。
输出描述:
每组数据输出一个表示最大的整数。
输入:
2
12 123
4
7 13 4 246
输出:
12312
7424613
"""

if __name__ == '__main__':
    a = int(input())
    inp_list=[]
    b = input()
    inp_list=b.split()
    assert len(inp_list)==a
    inp_list=(sorted(inp_list,reverse=True))
    idx=0
    while(idx<len(inp_list)-1):
        str1=inp_list[idx]
        str2=inp_list[idx+1]
        if len(str1)>len(str2) and str1[:len(str2)]==str2:
            combine_12=int(str1+str2)
            combine_21=int(str2+str1)
            if combine_12>=combine_21:
                 idx+=1
            else:
                tep=inp_list[idx]
                inp_list[idx]=inp_list[idx+1]
                inp_list[idx+1]=tep
                idx=0
        else:
            idx+=1
    print(int(''.join(inp_list)))
