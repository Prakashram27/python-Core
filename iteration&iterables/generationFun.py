def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3           
  
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


#output:
# 1
# 2
# 3

# Generator functions return a generator object. 
# Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop (as shown in the above program). 


#USING NEXT KEYWORD

# A Python program to demonstrate use of
# generator object with next()
 
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))


#Laziness and The infinity

def lucas():
    yield 2
    a =2
    b = 1
    while True:
        yield b 
        a,b = b,a+b 

for x in lucas():
    print(x)