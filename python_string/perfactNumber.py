def perfactNumber(n):
	sum=0
	for i in range(1,n):
		if(n%i)==0:
			sum=sum+i
	if(sum==n):
		print(n,'is perfact number')
	else:
		print(n,"is not perfact number")
n=int(input("enter the number"))
perfactNumber(n)		