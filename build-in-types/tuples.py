empty_tuple = ()
print(type(empty_tuple))  #<class 'tuple'>

int_tuple = (1,2,3,4,5,6,7,8)

# creating mixed data type 
mixed_tuple = (4, "Python", 9.3)    
    
# Creating a nested tuple    
nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))    

# Python program to create a tuple without using parentheses    

tuple_ = 4, 5.7, "Tuples", ["Python", "Tuples"]    
print(tuple_)   #(4, 5.7, 'Tuples', ['Python', 'Tuples'])
print(type(tuple_))  #<class 'tuple'>

# create a tuple having a single element    
single_tuple = ("Tuple")    
print( type(single_tuple) )                         #<class 'str'>
# Creating a tuple that has only one element    
single_tuple = ("Tuple",)    
print( type(single_tuple) )                         # <class 'tuple'>
# Creating tuple without parentheses    
single_tuple = "Tuple",    
print( type(single_tuple) )                       #<class 'tuple'>




#Accessing element in tuples
print(int_tuple[0])   # 1 

print(len(int_tuple))   # 8  --> helps to find the length of tuple.


#iterating
for item in int_tuple:
    print(item)

#Output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

concatination_tuple =  int_tuple + (20,)
print(int_tuple)  #(1, 2, 3, 4, 5, 6, 7, 8)
print(concatination_tuple) #(1, 2, 3, 4, 5, 6, 7, 8,20)



concat2 = mixed_tuple * 3
print(concat2)  #(4, 'Python', 9.3, 4, 'Python', 9.3, 4, 'Python', 9.3)


#Accessing nested type tuples

nested_tuple_ =  ((220,284),(1184,1210),(2620,29),(30,36))
print(nested_tuple_[0][1]) 
#output
# 284 

# n some cases single element tuple will be assign.. in that way we should use comma separated

single_tuple_elemet = (113,)   #parsed as a single element tuple
print(type(single_tuple_elemet))  #<class 'tuple'>

incorrect_format = (400)
print(type(incorrect_format))  #<class 'int'>

without_paranthesis = 1,2,3,4,5,6
print(type(without_paranthesis)) #<class 'tuple'>


def minmax(items):
    return min(items),max(items)

print(minmax([83,91,27,24,53,33,80]))  #(24, 91)


# tuple unpacking 
minValue, maxValue = minmax([83,91,27,24,53,33,80]) #here the single element value assigned into single variable object

print(minValue,maxValue)


(a,(b,(c,d))) = (1,(2,(3,5)))
print(a,b,c,d) #1 2 3 5


ab = 'jelly'
cd = 'bean'

ab,cd = cd,ab
print(ab) #bean #swabbed

# tuple constructor 

constructed_tuple =  tuple([10,20,30,30,40])
print(constructed_tuple)  #(10, 20, 30, 30, 40)

constructed_tuple2 = tuple('caramel')
print(constructed_tuple2)    #('c', 'a', 'r', 'a', 'm', 'e', 'l')





