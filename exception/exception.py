

# SyntaxError
# try:
#    You do your operations here
#    ......................
# except1:
#    If there is any exception, then execute this block.
#    ......................
# except2:
#    If there is any exception, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block. 



a = 5 
b = 10

k = int(input("Enter a Number"))

try:
    fh = open("testfile", "w")
    print(a/k)
except ZeroDivisionError as e:
    print('Cannot divide a number by Zero',e)

    #here e is except object to get exact error type
except ValueError as e:
    print('Invalid Input')
except Exception as e:
    print('Unknown error')

finally:
    fh.close() # this code will run if exception occurs



# The except Clause with Multiple Exceptions

# try:
#    You do your operations here
#    ......................
# except(Exception1[, Exception2[,...ExceptionN]]]):
#    If there is any exception from the given exception list, 
#    then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block. 


#Raise exception

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")




