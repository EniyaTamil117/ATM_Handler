print("Welcome to ABC Bank\n\nInsert Your Card")

password=1234
balance=10000
choice=0

pin=int(input("Enter your Four Digit Pin\n"))

if pin==password:

    while choice !=4:

        print("\n\n**** Menu ****")
        print("1 ==Balance==")
        print("2 ==Deposit==")
        print("3 ==Withdraw==")
        print("4 ==Cancel==")
        
        choice=int(input("Enter your Option:"))
        
        if choice==1:
            print("Balance = Rs.",balance)
        elif choice==2:
            dep=int(input("Enter Your deposits: Rs."))
            balance += dep
            print("\nDeposited amount: Rs.",dep)
            print("Balance = Rs.",balance)
        elif choice==3:
            wit=int(input("Enter the amount to withdraw: Rs."))
            balance -= wit
            print("\nWithdrawn Amount: Rs.",wit)
            print("Balance = Rs.",balance)
        elif choice==4:
            print("\n Session Ended!! Goodbye")
        else:
                print("invalid Entry!!")     


else:
    print("Incorrect Pin!! Try Again")