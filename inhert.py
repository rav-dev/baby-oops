#simple inheritence

# BASE CLASS 

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


# DERIVED CLASS

class Dog(Animal):

    def __init__(self):
        self.behaviour = "friendly"
    #here the speak method is overridden in the Dog class


    #this is also an example of method overloading becasue same method but child class has 
    #its own character so python will execute child's method not the parents method.
    def speak(self):
        #print(f"{self.name} barks") #its is using self.name attribute of animal class
        #print(f"Buddy barks. He is very {self.behaviour}") #this will run when the Dog obj calls
        print(f"{self.name}barks. He is very {self.behaviour}") #this will not run saysing the Dog
            #obj has no attribute name even though Dog is inheriting the Animal class. This is called
            #constructor overloading. So when there is a constructor in the child class and by default 
            #we have initiated the attribute then python wont consider parents constructor attributes
    #def speak1(self):
    #    print(f"{self.name} barks")


# create an instance of Animal class 

#animal = Animal("generic Animal")
#animal.speak()

# create an instance of a dog class 
#dog = Dog("Buddy") #dog class is inhetiting Animal class and Animal class needs a name 
                   #during object creation


#although Dog class does not have the speak method, but it inherits the attributes as well as the 
#methods of the parent class. So it will execute the method of the parent class
#dog.speak()




#needed of inheritence 

#ttcode usability. Lets say the parent class is college. Attributes- affiliated to which uni, 
#college name, college time, college address. So may be student might belong to different courses
#pays a different fee or in different year in college, but the basic college attributes for him
#will be same. So in such a case we can use inheritence where we can make student inherits college 
#class so auto he gets access to all the basic college related attributes.


#the parent class has no access to the child class. Child can access the parents attributes but
#not vice versa. 


#a child class can inherit -> constuctors, non private attributes and methods



#constructor overloading

dog = Dog() 
dog.speak()