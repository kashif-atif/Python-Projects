from random import choices


print ("atm machine")

passkey = 1234
amount = 1000
userkey = int(input("enter passkey"))

if userkey == passkey:

    print ("what do you want ")
    print ("1 : withdraw")
    print ("2 : deposite") 
    print ("3 : check balance")

    choices = int(input("enter choice from above"))
    if choices == 1:
        print ("withdraw amount please")
        a = int (input ("enetr amount"))
        if a <= amount :
            print (f"you withdraw {a} now your balance is {amount - a }")
        else :
            print ("insufficiant balance")


    elif choices == 2:
        print ("deposite amount ")
        b = int(input("enter deposite amount "))
        print (f"you deposite {b} now your balance is {amount + b}")


    elif choices == 3:
        print (f"your current balance is {amount}")  

    else :
        print ("insufficiant choice ")


else :
    print ("your passsword is wrong")
