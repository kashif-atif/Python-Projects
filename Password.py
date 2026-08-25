import random
def password_generator(lenght):
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%"
    password = ""

     
    for i in range(lenght):
       password += random.choice(char)

    return password

lenght = int(input("enter number")) 
password = password_generator(lenght)
print (password)
