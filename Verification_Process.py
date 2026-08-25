print ("                      AGE VERIFICATION PROCESS                  ")

i = int (input("enter your age"))
if (i>=18):
   print ("you are verified successfully")
else:
   print ("you are under age")
while (i<18):
   i = int (input(" please enter your age again"))
   i = i+1 
else :
   print ("you are verified successfully")

print ("NOW PLEASE ENTER YOUR USERNAME")
name = input("enter your username: ")
print ("WELCOME TO OUR PAGE, " + name)



print ("ENTER YOUR MOBILE NUMBER")
mobile = input("enter your mobile number: ")
if (len(mobile) == 11):
   print ("your mobile number is verified successfully")
else :
   print ("your mobile number is not valid")
   mobile = input("enter your mobile number again: ")
    
while (len(mobile) != 11):
   mobile = input(" please enter your mobile number again ")
else :
   print ("your mobile number is verified successfully")

   print ("what is your gender?")
   print ("1. male")
   print ("2. female")
   print ("3. other")
   gender = int(input("choose your gender (1/2/3): "))
   if (gender == 1):
      print ("you are male")
   elif (gender == 2):
      print ("you are female")
   elif (gender == 3):
      print ("you are other") 
   else :
      print ("please enter a valid response")


   print ("                     THANK YOU FOR VISITING OUR PAGE              ")

a = input(("do you want to visit again? (yes/no): "))
if (a == "yes"):
      print ("WELCOME TO OUR PAGE, " + name)
elif  (a == "no"): 
      print ("we repect your response thank")
else :
      print ("please enter a valid response")
         
