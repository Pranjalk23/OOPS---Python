class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        user_input = input("""Welcome to Chatbook!
                           1. Press 1 to SignUp
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        if user_input == "1":
            self.SignUp()
        elif user_input == "2":
            self.Signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
            
        
    def SignUp(self):
        email = input("Enter the Username or email :")
        pwd = input("Create a password :")
        self.username = email
        self.password = pwd
        print("You can now login!")
        print("\n")
        self.menu()
        
    def Signin(self):
        if self.username == '' and self.password == '' :
            print("Pls, Signupfirst")
            self.menu()
        else:
              uname =input("Enter the username or email :")
              pwd = input("Enter the password :")
              self.username = uname
              self.password = pwd
        
        if self.username == uname and self.password == pwd :
            print("You have succesfully logged in!")
            self.loggedin = True
        else:
            print("Enter correct credentials")
        print("\n")
        self.menu()
            
obj = chatbook()