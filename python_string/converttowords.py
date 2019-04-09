def convert_to_words(num):
    l = len(num);
    if (l == 0): 
        print("empty string"); 
        return; 
  
    if (l > 4): 
        print("Length more than 4 is not supported"); 
        return; 
  
    # The first string is not used,  
    # it is to make array indexing simple  
    single_digits = ["zero", "one", "two", "three",  
                     "four", "five", "six", "seven",  
                     "eight", "nine"]; 
  
    # The first string is not used,  
    # it is to make array indexing simple  
    two_digits = ["", "ten", "eleven", "twelve",  
                  "thirteen", "fourteen", "fifteen",  
                  "sixteen", "seventeen", "eighteen", 
                  "nineteen"]; 
    tens_multiple = ["", "", "twenty", "thirty", "forty", 
                     "fifty", "sixty", "seventy", "eighty",  
                     "ninety"]; 
  
    tens_power = ["hundred", "thousand"]; 
  
    # Used for debugging purpose only  
    print(num); 
  
    # For single digit number  
    if (l == 1):  
        print(single_digits[ord(num[0]) - '0']); 
        return; 
  
    # Iterate while num is not '\0'  
    x = 0; 
    while (x < len(num)):
        if (l >= 3): 
            if (ord(num[x]) - 48 != 0): 
                print(single_digits[ord(num[x]) - 48])  
                                         
                print(tens_power[l - 3]);  
               
                  
            l -= 1; 
              
        # Code path for last 2 digits 
        else: 
            if (ord(num[x]) - 48 == 1):  
                sum = (ord(num[x]) - 48 + 
                       ord(num[x]) - 48); 
                print(two_digits[sum]); 
                return; 
            else: 
                i = ord(num[x]) - 48; 
                if(i > 0): 
                    print(tens_multiple[i]); 
                else: 
                    print(""); 
                x += 1; 
                if(ord(num[x]) - 48 != 0): 
                    print(single_digits[ord(num[x]) - 48]); 
        x += 1; 
  
# Driver Code 
convert_to_words("9923"); 
convert_to_words("523"); 
convert_to_words("89"); 