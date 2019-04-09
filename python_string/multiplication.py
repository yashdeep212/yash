def multiplication(list1):
	result=1
	for i in list1:
		if(type(i)==str):pass
		else:
			result=result*i
	print(result)
list1=["yash",-1,-2,3,4,5,"deep"]
multiplication(list1)