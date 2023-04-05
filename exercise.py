
#Method1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

my_dict = dict(zip(list1, list2))
print(my_dict)


#method2

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

my_dict = {list1[i]: list2[i] for i in range(len(list1))}
print(my_dict)



#method 3 

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

my_dict = dict(zip(list1, list2))

# Get the keys and values as separate lists
keys = my_dict.keys()
values = my_dict.values()

# Create a new dictionary using the key and value lists
new_dict = dict(zip(values, keys))
print(new_dict)



# method 4 



