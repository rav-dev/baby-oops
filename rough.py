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

#user1 = chatbook()

#lst = [1,2,3]

#function 
#to use the func we directly call the func 
#a1 = len(lst)
#print(a1)

#when we call a method then we cant use it directly we have to call it via class object 
#user1 = chatbook()
#user1.sendmsg()


#there may be some situation where we do not want user to access all the attributes or methods
#of the class. Eg the connection attributes mentioned in the constructor or 
#some methods that are working or using some sensitive infor eg credentials.
#so we would like to hide it from the user -> encapsulation

#user1 = chatbook()

#print(user1.__name) #ttributeError: 'chatbook' object has no attribute '__name'
#we cannot fully protect any attribute or method in python. 

#print(user1.chatbook.__name)

#getter setter methods 
#sometimes we need to define the functionality in the module so that the user can access
#the protected variables or methods. so for that we use getter and setter methods
#user1.set_name("rjbir")
#print(user1.get_name())


#so far we can create as many users obj of chatbook class as we want, but what if we assign unique id
#to the objects

#user1 = chatbook()
#print(user1.id)

#user2 = chatbook()
#print(user2.id)

#user3 = chatbook()
#print(user3.id)


#static

user1 = chatbook()
print(user1.id)

#using static method directoy from the class rather than the obj
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)