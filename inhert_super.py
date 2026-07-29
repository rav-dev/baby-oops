class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):

    #we have constructor here so upar ka constructor nahi call hoga but still hame kuch attributed
    #chahiye parent class se so we use super().func(dunder func or normal func) 
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed}")
        #self.name attribute hum super() ki wajah se kar pa rahe hai access because super se 
        #humne poora parent class ka constructor call kiya



dog = Dog("Golden retriever")
dog.speak()



#super can only be used inside the child class meaning we cannot call parent class attribute 
#outside the class 


#dog.super().speak() #ye nahi kar sakte obj mein super nahi laga sakte

#super cannot access variables to methods hi call karo super se 