def is_prime(x):
  if x == 0:
    return False 
  if x == 1:
    return False
  if x == 2:
    return True
  if x == 3:
    return True
  else:
    x = abs(x)
    for n in range(2, (x-1)):
      print x
      if ((x % n) == 0):
        return False		
    else:
      return True