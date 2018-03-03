def factorial(x): #a function that take an input of x 
  if(x==0): #failure case of x == 0 
    return 1 #return 1
  else:  
    a=1  #initialize a value to 1 
    z=1  #initialize z value to 1 
    while a<=x: #while a is less than or = to x
      z*=a #z = z * a 
      a+=1 #a = a + 1
    return z #return z
