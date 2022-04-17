from ast import And
from os import remove
from turtle import clear
from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file = open("key.key","rb")
    key=file.read()
    file.close
    return key


pwd=input("Enter master key:")
key = load_key() + pwd.encode()
fer = Fernet(key)




def add():
    name = input('Account Name:')
    password = input("Password:")
    
    with open('password.txt','a') as a:
        a.write(name +"|"+fer.encrypt(password.encode()).decode()+"\n")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user,"\nPassword:",fer.decrypt(passw.encode()).decode(),"\n")


while True:    
    x = input("Do you want to:\n1.Add a new password \n2.view existing ones?\n3.press q to quit\n").lower()
    if x=="q":
        break
    if x=="1":
        add()
    elif x=="2":
        view()        
    else:
        print("Invalid Mode")
        continue 