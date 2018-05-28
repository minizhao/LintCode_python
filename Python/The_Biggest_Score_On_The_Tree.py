


def dfs(node,curr_cost,sum,tree,profit):
	#是叶子节点
	if node not in tree.keys() :
		return sum+profit[node]-curr_cost

	sum=sum+profit[node]-curr_cost

	childs=tree[node]

	sum_list=[]
	for c,cost in childs:
		sum_list.append(dfs(c,cost,sum,tree,profit))
	return max(sum_list)


def make_tree(x,y,cost):
	tree={}
	for x,y,c in zip(x,y,cost):
		if x not in tree.keys():
			tree[x]=[(y,c)]
		else:
			tree[x].append((y,c))
	return tree

if __name__ == '__main__':
	tree=make_tree(x=[0,1,2,3,3,3,1,7,1],y=[1,2,3,4,5,6,7,8,9],cost=[47,48,44,95,84,61,51,86,43])
	rst=dfs(0,0,0,tree,[77,41,27,19,71,17,35,84,61,2])
	print(rst)




