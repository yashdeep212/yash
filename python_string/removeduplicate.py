def removeduplicate(list1):
	temp=0
	list1=list(set(list1))
	list1.sort()
	print(list1)
	# for i in list1:
	# 	for j in list1:
	# 		if(list1[i]==list1[j]):
	# 			list1.remove(list1[i])
	# 		else:
	# 			print(list1)

list1=[1,-3,5,7,1,5]	
removeduplicate(list1)	