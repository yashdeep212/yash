def wordLength():
    	pass    
    wordcount={}
    for word in st.split():        
        key = len(word)

        if key not in wordcount:
            wordcount[key] = 1
            
        else:
            wordcount[key] += 1
    for k,v in wordcount.items():
        print (k, v)
    return None   
wordLength("i my a yash n this is")