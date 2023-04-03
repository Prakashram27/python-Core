words = ' you can use to create powerful functionality within a single line of code'.split()
print(words)

print([len(word) for word in words])


#List comprahensions syntax 
# [exp(item) for item in iterable]

#Equivalent sytax

length =[]
for word in words:
    length.append(len(word))

print(length)

from math import factorial
f = [len(str(factorial(x))) for x in range(20)]

print(f) #[1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]

print(type(f))  #<class 'list'>



# SET COMP 

s = {len(str(factorial(x))) for x in range(20)}
print(s)
print(type(s))



# DICT COMP 

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)
 

#syntax
# {
#  key_exp(item) : value_exp(item)
# for item in iterable
# }

capital_to_country = {
    'UK':'London',
    'brazil':   'brazilia',
    'moracco':'rabt',
    'sweden ': 'stockhome'
}

capital_to_country = {capital:country for country, capital in capital_to_country.items()}
from pprint import pprint as pp

print(pp(capital_to_country))


words = ['hi','hello','welcome','Thankyou']
print({
    x[0]:x for x in words
})



# FILTER COMP 

even = [x for x in range(10) if x % 2 == 0]
print(even)

#Ex2

from math import sqrt
def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(sqrt(x)) + 1):
        if x%i == 0 :
            return False
    return True

prime = [x for x in range(101) if is_prime(x)]
print(prime)



# Iteration protocol

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('iterable is empty')
    
print(first(['1','2','3']))
print(first({'1','2','3'}))
# print(first(set()))



def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30



