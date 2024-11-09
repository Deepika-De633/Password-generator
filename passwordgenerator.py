import random
letters=["A","B","C","D","E","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digits=[1,2,3,4,5,6,7,8,9,0]
symbols=["!","@","#","$","%","*","/"]
n_letters=int(input("How many letters do you wanbt to include in the password?"))
n_digits=int(input("The  number diits do you wan to include in the password?"))
n_symbols=int(input("the number of symbols do you want to include in t he password?"))
generated_password=[]
for char in range(1,n_letters+1):
    generated_password.append(random.choice(letters))
for i in range(1,n_digits+1):
    generated_password.append(random.choice(digits))
for char in range(1,n_symbols):
    generated_password.append(random.choice(symbols))
print(generated_password)
random.shuffle(generated_password)
print(generated_password)
password=" "
for char in generated_password:
    password += str(char)
print(f"THE FINAL PASSWORD IS:{password}")
