import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pwd():
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    pwd = ""

    for char in range(1, nr_letters + 1):
        pwd += random.choice(letters)

    for char in range(1, nr_numbers + 1):
        pwd += random.choice(numbers)

    for char in range(1, nr_symbols + 1):
        pwd += random.choice(symbols)

    password = list(pwd) 
    random.shuffle(password)
    pwd = "".join(password)
    return pwd

     
