
x= 12000  
print(type(x))

x = 'Dynamic Typing'  
print(type(x))    

x = [1, 2, 3, 4]  
print(type(x))  

# output
        # <class 'int'>
        # <class 'str'>
        # <class 'list'>

students = ['Emma', 'Jessa', 'Kelly']
school = 'ABC School'

# calculate count
print(len(students))
print(len(school))


# Inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)



class Person:
  def __init__(self,fname,lname):
    self._firstname = fname
    self.lastname = lname
  def printName(self):
    print(self._firstname,self.lastname)

class Student(Person):
  def __init__(self,fname,lname, year):
    Person.__init__(self,fname,lname)
    self.graduationYear = year

s1 = Student("Prakash","Ramu",2022)
s1.printName()
print(s1.graduationYear)