class ATM:
    def __init__(self):
        self.pin="1234"
        self.balance=1000
        self.password=int(input("enter your atm pin"))
        if self.password==int(self.pin):
            while True:
                self.user_input=input('''
        Welcome
                                    Enter 1 for change pin
                                    Enter 2 for checking balance
                                    Enter 3 to deposit
                                    Enter 4 to withdraw
                                    Enter 5 to Exit
        ''')       

                if(self.user_input=="1"):
                    self.create_pin()
                elif(self.user_input=="2"):
                    self.check_balance()
                elif(self.user_input=="3"):
                    self.deposit()
                elif(self.user_input=="4"):
                    self.withdraw()
                elif(self.user_input=="5"):
                    print("Bye")
                    break
                else:
                    print("try again")
        else:
            print("Try Again\nEnter valid password")


    def create_pin(self):
        self.pin=input("enter your pin:")
        print("Pin created successfully")


    def check_balance(self):
        self.password=input("enter pin:")
        if(self.password==self.pin):
            print(f"Your current balance is{self.balance}")

        else:
            print("Invalid Pin")


    def deposit(self):
        self.password=input("enter you pin:")
        if(self.password==self.pin):
            self.dep=int(input("enter the amout to deposit:"))
            self.balance=self.balance+self.dep
            print(f"Your amount {self.dep} is deposited successfully")

        else:
            print("Invalid Pin")

    def withdraw(self):
        self.password=input("enter pin:")
        if(self.password == self.pin):
            self.with_draw=int(input("enter the amount to withdraw:"))
            if(self.with_draw <= self.balance):
                self.balance=self.balance-self.with_draw
                print("withdrawal successfull")
            else:
                print("Amount not enough to withdraw")






sbi=ATM()


