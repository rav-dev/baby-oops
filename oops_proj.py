class chatbook:
    def __init__(self):
        self.user_name = ''
        self.password = ''
        self.loggedin = False
        #as soon as the object is created we will call the menu
        self.menu()

    def menu(self):
        """describe the main menu
        """
        user_input = input("""welcome to chatbook !! how would you like to proceed?
        1. press 1 to signup
        2. press to 2 to signin
        3. press 3 to write a post
        4. press 4 to message a friend
        5. press any other key to exit""")

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
                    pass
        elif user_input == "4":
                    pass
        else:
              exit()
        



obj = chatbook()