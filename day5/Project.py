print ("Wellcome to the PyPassword Generator! ")
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbol = int(input("How many symbols would you like?\n"))
nr_number = int(input("How many numbers would you like?\n"))
password_list = []
for char in range(0,nr_letter):
    password_list.append(random.choice(letters))
for char in range(0,nr_number):
    password_list.append(random.choice(numbers))
for char in range(0,nr_symbol):
    password_list.append(random.choice(symbols))
# hàm shuffle dùng để xóa trộn list 
random.shuffle(password_list)
password =""
for char in password_list:
    password += char
print(f"Your password is {password}")