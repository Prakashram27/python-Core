#determining length of the string

print(len('hello')) #5

#concatination
print('Happy' + ' New'+ ' Year')  #Happy New Year

#Using assignment operator

s = "New"
s += "Welcome" 
print(s)

#strings are immutable. we cannot modify them in place


#str.join()

# Joining with empty separator
list1 = ['M', 'a', 'a', 's']
print("".join(list1))
print(type(list1)) #list

# Joining with string
list1 = " Mass "

joinFun =  "$".join(list1)

print(type(list1)) #str

print(joinFun.split('$'))


print('unforgatable'.partition('forgat')) # ('un', 'forgat', 'able') # returns in tuple

partitionString =  depecture,separator,arrival = "partialElegent".partition('Ele')
print(depecture)


# string interpolation 
print(f"one plus one is{1+1}")

print('hello {1+1}') #it will consider as string

#we can find string method using following code
# help(str)


# RANGE()

print(list(range(0)))  
  
# using the range(stop)  
print(list(range(4)))  
  
# using the range(start, stop)  
print(list(range(1,7 )))  

#output
[]
[0, 1, 2, 3]
[1, 2, 3, 4, 5, 6]