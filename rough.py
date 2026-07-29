lst = [1,2,3]
my_str = "mlops play"
my_int = 155

#print(type(lst)) #<class 'list'> inbuilt python list class 
#print(type(my_str)) #<class 'str'>

a = 'x'
b = 'y'

print(a+b) #in output we get concatination xy not x+y
#but using OOP we can make such data types where when we do the above operation we get get x+y instead of 
#string concatination

#anything in python whether it is a string or any data structure are all object
#of inbuilt classes in python 

#adv of OOPS 
# - you can create your own datatype 
# - code reusability == preprocessing class can be used in other similar projects dealing with similar data
# - debugging == easiy to identify in which class and in which method we are getting the error
# -easy to colab




#we will be using the obj_prod module
#we will import the chatbook class from oops_proj module

from oops_proj import chatbook

user1 = chatbook()

