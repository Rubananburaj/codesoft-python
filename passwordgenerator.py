import random
import string

def generate_password(length):
   """ string.ascii_letters: This constant is a string containing all ASCII letters, both lowercase and uppercase.
    It is equivalent to concatenating string.ascii_lowercase and string.ascii_uppercase.
        For example, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"."""

#string.digits: This constant is a string containing the digits "0123456789".

#string.punctuation: This constant is a string containing ASCII characters considered as punctuation, such as !"#$%&'()*+,-./:;<=>?@[]^_`{|}~.

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


    
