def caseOfString(s1):
	count=0
	count2=0
	for i in s1:
		if(i.isupper()):
			count+=1
		elif(i.islower()):
			count2+=1
	print("uppercase----",count)
	print("lowercase----",count2)

s1="This Is MyTaSK and "
caseOfString(s1)