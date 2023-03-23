stringData = 'Hello' #single quotes
stringDouleQuoteUse = "Hello hi" #double quotes

stringDouleQuoteUse= "world" # updated here

print(stringDouleQuoteUse)

#inconsistent = "hello' inconsistent style

# consistent ways
a = "Lorem ipsum dolor sit amet,consectetur adipiscing elit, sed do eiusmod tempor incididuntut labore et dolore magna aliqua."
print(a)


fString = "hello"
#fString[1] = "r"  #TypeError: 'str' object does not support item assignment
print(fString)


#STRING LITERALS 

"first" "second" # firstsecond

print("""Hello
   hi
   this is mltiple line 
   string""")  #Here we can use \r\n(windows) \n (linux)

print(
    "Hello\nhi\nthis is mltiple line\nstring"
) 



# A string with a recognized escape sequence
print("I will go\tHome")
 
print("See you \' tommorow")
print("See you  tommorow")


rawString = r'C:\user\prakash'  # we can add r'' for raw prefixes.
print(rawString)

str(489) #converting to string "498"
str(6.02e+23) #"6.02e+23"

s = 'parrot'
print(s[4]) # accessing individual cherecter by using index value

print(type(s[4]))  #<class 'str'>

#print(help(str)) # to know the features in string 


c = 'hello'

print(c.capitalize()) #not mtating original string
print(c.upper())
print(c.lower())





