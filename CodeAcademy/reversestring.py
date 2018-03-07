def reverse(text): #defines a function called reverse that accepts a string input called text
  p = [] #initalizes an empty list
  y = (len(text)-1) #sets the variable y to the length of the string - 1 

  for i in text: #a for loop that iterates i times through the variable text
    p.append(text[y]) #appends the value of text[y] the list p
    print p #prints p for sanity
    print y #prints y for sanity
    y = y - 1 # decrement y for each loop
  str1 = ''.join(p) #join the list, remove spaces and convert the string
  return str1 #return the string
