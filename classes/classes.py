
class Person:
    pass

# having an empty class definition like this, would raise an error without the pass statement

# class Airflight:

#     def number(self):
#         return 'S16012'
    
# f = Airflight()

# print(f.number())  #method I 

# print(Airflight.number(f)) #method II



class Employees:
    def __init__(self,number):        #__init__ function initializer for creating new object #should not return anything
        self._number = number         #here _number is attribute 
    def number(self):
        # return 'ID123'     # instead we can return self._number
        return self._number
    

E1 = Employees('ID1234')
E2 = Employees('ID1235')
print(E1.number())
print(E2.number())
#Here why we are using _number attribute
        # name clash with the method of same name  ---> number()

# print(E1._number)    # not recommended
# print(E2._number)



# INVARIENTS

class Flight:
    def __init__(self,number):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')
        if not number[:2].isupper():
            raise ValueError(f'Invalid value error "{number}"')
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError (f'Invalid route "{number}"')         
        self._number = number

    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]
    
    

FN = Flight('SN123')
print(FN.number())
F2= Flight("NS123")
print(F2.airline())



class Aircraft:
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seat_per_row = num_seats_per_row
    
    def registration(self):
        return self._registration
    def model(self):
        return self._model
    def seat_planning(self):
        return (range(1,self._num_rows +1), 'ABCDEFGHIJ'[:self._num_seat_per_row]  ) 
    
a = Aircraft("G-EUPT","Airbus A31", num_rows=22,num_seats_per_row=6)

print(a.registration())
print(a.model())
print(a.seat_planning())


    # Output 
    # G-EUPT
    # Airbus A31
    # (range(1, 23), 'ABCDEF')






