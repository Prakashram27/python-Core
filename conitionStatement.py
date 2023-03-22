#CONDITION STATEMENTS

# syntax if keyword followed by expressiom and terminated by  colon and the block of statement 
# if expression:
#     Block


h = 42
if h>50:
    print("Greater") 
else :
    if h > 20:
      print("less rhan 20")
    elif h <10:
     print("less than 10")


#WHILE LOOP

# syntax 
# while expression:
#     statement(s)

c =5

while c !=0:
   print(c)
   c -= 1  

   # output 5 4 3 2 1 

c =5

while c:
   print(c)
   c -= 1  

   # output 5 4 3 2 1 
   #this is works becoz this expression run still bool(0): false


