def palindrom(s1):
	rev=s1[::-1]		
	if(s1==rev):
		print("string is palindrom")
	else:
		print("string is not palindrom")
		
s1="111222111222111"
palindrom(s1)