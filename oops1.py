#initiate a class 

class employee:
    #sp or magic method or dunder method
    #method used to define the data attributes of the class is called the constructor

    #we use constructor to define some functionalities that we do not want 
    #the user to do it while interacting with our program
    #eg DB connnections, we do not want user to create DB connection manually 
    #while using our program, so we can describe such functionality in the
    #constructor
    def __init__(self):
        print("started executing attributes and data")
        print(id(self)) #memory address of self obj
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes data have been initiated")

    def travel(self,destination):
        print("this travel function was called intentionally")
        print(f"Employee is now traveling {destination}") 

#creating the instance of the class 
#whenever we initialized the object then the constructor obj is created auto
#sam = employee()
#jamie = employee()

#two objects of same class will not have same address they will be stored at different location
#in the memory. Subsequentlky self will also exhibit different memory address for both the objects
#print(f"the memory address of sam obj is {id(sam)}")
#print(f"the memory address of jamie obj is {id(jamie)}")


"""the memory address of self and sam obj is same. 
    Whatever obj we are making of the class self is that obj. 
    we pass the obj in constructor so self is just a reference to the obj name we have created. 
    that is why in methods also it is mandatory to pass the obj becasue only obj is allowed to 
    interact or access the class attributes and methods
"""



#calling a method
#sam.travel("kerala")

#printing an attributes
#print(sam.salary)

#print(type(sam)) #<class '__main__.employee'>




#you can create attribute outside class as well. 

#sam = employee()
#sam.name = "sam kumar"
#print(sam.name)