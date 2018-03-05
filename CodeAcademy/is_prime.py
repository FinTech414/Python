def is_prime(x): #define a function that takes one parameter x
  if x < 2: #Checks if x is less than 2, any number less than 2 is considered False and not prime
    return False #return False since its less than 2
  if x > 2: # if x is greater than 2, run a check to see if anything is modulo zero against it
    for n in range(2, x): # create a for loop with the range of starting at 2 (first non prime) to the value of x.  actually x-1 since range will stop before it
      if x % n == 0: 
        return False #if modulo of x % n is equal to zero then you know it is divisible and is not prime
  return True #else return True 
