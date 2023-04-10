"""Write a Python Program to Swap the First and Last Value of a List?"""

list = [1,2,3,4,5]
def swab_first_letter(lst):
    temp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp
swab_first_letter(list)
print(list)  

"""Dict"""
dict_ =  { i:i for i in range(1,10)}
print(dict_)


"""Write a Python Program to Check Common Letters in Two Input Strings?"""
string1 = 'hello'
string2 = 'welcome'
common = []
con_str1 = [x for x in string1]
con_str2 = [x for x in string2]

for i in con_str1:
    for j in con_str2:
        if i == j and i not in common:
            common.append(i)
print(common)
        
"""Create a dictionary using while loop? For example student name and roll number?"""

student = ['Arun','Akash','Ajay']
roll_no = ['01','02','03']
com_method = {student[x]:roll_no[x] for x in range(0,len(student))}
print(com_method)



# initial = 0
# second = 1
# fib = []
# while initial > 100:
#     if initial not in fib:
#         fib.append(initial)
#         continue
#     elif second not in fib:
#         fib.append(second)
# print(fib)
