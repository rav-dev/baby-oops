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
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes data have been initiated")

    def travel(self,destination):
        print("this travel function was called intentionally")
        print(f"Employee is now traveling {destination}") 

#creating the instance of the class 
#whenever we initialized the object then the constructor obj is created auto
sam = employee()
#calling a method
#sam.travel("kerala")

#printing an attributes
#print(sam.salary)

print(type(sam)) #<class '__main__.employee'>



