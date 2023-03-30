#Assigning to a variable
x = 1000
#here  python created an int object with a value of 1000.

x = 500

#integer objects cannot be changed.. Immutable
#here python created a new immutable int object and redirects variable value in 500. x reference points to the new object
#finally the python garbage collecter will reclaim it at same point.


y = x
 
#when we assign one varible to another assigning one object reference from another object reference
#both reference will point the same object

x = 3000

#here y reference point to the 500 int value object. x reference point to the value 3000 object



# id() function 
#return a unique integer identifier for an object.

print(id(x))  #140166730087248
print(id(y))  #140166730087312

a = 10
b = 10

print(id(a))
print(id(b))

print(id(x) == id(y)) #False
print(id(a) == id(b)) #True

print(a is None)  #False

#Mutable Object
r = [1,2,3]
s = r
s[1] = 'changed'  
print(r) #[1, 'changed', 3] #reference by id
print(s) #[1, 'changed', 3]


print(r is s) # True

# VALUE VS IDENTITY EQUALITY
p = [1,3,4]
q = [1,3,4]

print(p==q) #True
print(p is q) #False


# PASSING ARGUEMENTS AND RETURNING VALUE 
m1 = [9,15,24]
def modify(k):
    k.append(39)
    print(k)
    print(m1)
modify(m1)

# ml = [9,15,24,39] 

fl = [14,23,37]
def replace(g):
    g = [17,28,45]
    print("g=",g)  #overwritten and replaced here
replace(fl)

print(fl)  # [14,23,37] 

#MUTABLE ARGUMENTS

def replace_content(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g=",g)
fs=[1 , 2, 3]
replace_content(fs)


print(fs) # result [17, 28, 45] mutated using item changes



def f(d):
    return d

c= [6,10,6]
e = f(c)
print(c is e) # True

