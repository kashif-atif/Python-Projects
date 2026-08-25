while True:
    
    chat = input("you :")
    if chat == "hello" or chat == "hi" :
       print ("chatbot : hi iam chatbot what is your name")
       name = input("you :") 
       print (f"chat bot : hi {name} how are you")

    elif chat == "good"  :
       print (f"wow very well {name} so what you have in your dinner")
       lunch = input ("you :")
       if lunch == "pizza" or lunch == "burger"  or lunch == "baryani" :
          print ("yammi thats tasty")
       else :
        print (f"i cant understand {name}")

    elif chat == "bad" :
        print (f"oh so sorry to hear {name}")   
    
    elif chat == "bye" or chat == "goodbye" :
        print (f"chatbot : goodbye {name} take care")

    else :
        print ("i dont understand")
