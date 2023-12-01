def power(b,c):
 if c==0:
    	return 1
 elif c==1:
 	return b   	
 else:
   	return b*power(b,c-1)
b=int(input("enter the base number"))
c=int(input("enter the exponent number"))
result=power(b,c)
print(result)    
