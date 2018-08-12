
"""
#二进制表示
Example
For n = "3.72", return "ERROR".

For n = "3.5", return "11.1".

Tags Expand
String Cracking The Coding Interview Bit Manipulation

先解析整数再解析小数，规则不一样
"""

def Binary_Representation(str_n):
	if len(str_n)==0 or str_n=='0':
		return "0"
	if '.' not in str_n:
		return parseInteger(str_n)
	str_list=str_n.split('.')
	rst_decimal=parseDecimal(str_list[1])
	print(rst_decimal)
	if rst_decimal =="ERROR":
		return rst_decimal
	rst_int=parseInteger(str_list[0])
	if (rst_decimal==''):
		return rst_int
	return rst_int+'.'+rst_decimal

def parseInteger(num):

	if(len(num)==0 or num=='0'):
		return num
	num=int(num)
	rst=''
	while num!=0:
		rst=str(num%2)+rst
		num//=2
	return rst

def parseDecimal(num):
	if len(num)== 0 or num=='0':
		return ''
	num =float('0.'+num)
	#用来判断是否循环
	list_nums=[]
	rst=''
	while (num>0):
		if num in list_nums or len(rst)>32:
			return"ERROR"
		list_nums.append(num)
		if num*2>=1:
			rst=rst+'1'
			num=num*2-1
		else:
			rst=rst+'0'
			num=num*2
	return rst


if __name__ == '__main__':
	rst=Binary_Representation('1.0')
	print(rst)
