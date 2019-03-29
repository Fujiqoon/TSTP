def count_ch(strings):
	count_str={}
	for i in strings:
		if i in count_str:
			count_str[i]+=1
		else:
			count_str[i]=1
	print(count_str)

count_ch('apple')
