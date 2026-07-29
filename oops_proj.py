class chatbook:
    __user_id = 0#only class can access class variables not self. 

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User" #hidden attribute
        #self.user_id = 0
        #self.user_id += 1 #whenevrr the obj is created it will increment
        self.user_name = ''
        self.password = ''
        self.loggedin = False
        #as soon as the object is created we will call the menu
        #self.menu()

    #it is used to access the class vars no need to pass self 
    #as only class can access it not the obj 

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value

    
    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name = value


    def menu(self):
        """describe the main menu
        """
        user_input = input("""welcome to chatbook !! how would you like to proceed?
        1. press 1 to signup
        2. press to 2 to signin
        3. press 3 to write a post
        4. press 4 to message a friend
        5. press any other key to exit
        
        -> """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
              exit()

    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("set up your password here -> ")
        self.user_name = email
        self.password = pwd
        print("you have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        #check if the user already has the account or not 
        #if yes then we will sign in the user 
        #if not then we will redirect the user to sign up
        if self.user_name == '' and self.password == '':
            print("please sign up first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            pwd = input("enter you password here -> ")
            if self.user_name == uname and self.password == pwd:
                print("you have signed in successfully")
                self.loggedin = True
            else:
                print("please input the correct credentials...")
        print("\n")
        self.menu()

    def my_post(self):
        #signin kiya hoga tab true hi rahega logged in 
        if self.loggedin:
            txt = input("enter your message here -> ")
            print(f"following content has been posted ->{txt}")
        else:
            print("you need to sign in first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin:
            txt = input("enter your message here -> ")
            frnd = input("whom to send the msg? -> ")
            print(f"your message has been sent to {frnd}")
        else:
            print("you need to sign in first to post something...")
        print("\n")
        self.menu()
            


        




        


#usr1 = chatbook()