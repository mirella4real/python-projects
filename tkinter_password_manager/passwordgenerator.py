import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pwd():
    pwd = ""
    random_letters = "".join([random.choice(letters) for char in range(random.randint(8, 10))])
    pwd += random_letters
    random_numbers = "".join([random.choice(numbers) for char in range(random.randint(2, 4))])
    pwd += random_numbers
    random_symbols = "".join([random.choice(symbols) for char in range(random.randint(2, 4))])
    pwd += random_symbols
    password = list(pwd) 
    random.shuffle(password)
    pwd = "".join(password)
    return pwd

     
