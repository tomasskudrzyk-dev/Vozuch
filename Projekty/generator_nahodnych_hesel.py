import random
import string

def generate_password(length):
    if length < 12:
        raise ValueError("Délka hesla musí být alespoň 12 znaků.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    while True:
        try:
            length = int(input("Zadejte délku hesla (minimálně 12 znaků): "))
            password = generate_password(length)
            print(f"Vygenerované heslo: {password}")
            break
        except ValueError as e:
            print(e)
            print("Zkuste to znovu.")