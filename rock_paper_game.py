import random 

list = ["rock" , "paper" , "scissor"]
user = input("enter (rock , paper , scissor ").lower()
computer = random.choice(list)
print ("computer selects :"  , computer)

if user not in list :
    print ("invalid selection")

elif user == computer:
    print ("the match is tie")

elif (user == "rock" and computer == "scissor" or 
      user == "paper" and computer == "rock" or 
      user == "scissor" and computer == "paper"):
    print ("you won ")

else:
    print ("computer won") 
