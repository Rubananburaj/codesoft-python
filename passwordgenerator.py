import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = [random.choice(characters) for _ in range(length)]
    password = ''.join(password_list) 

    """  ''.join(...): This part joins the sequence of characters into a single string. 
    The '' (empty string) is the separator between the characters. 
    So, it concatenates the characters without any separator,
      effectively creating a random string of the specified length.  """ 
       
    return password

try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Please enter a positive length.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")


    