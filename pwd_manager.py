
from cryptography.fernet import Fernet
import getpass
import time



print('''
  _____                                    _    __  __                                   
 |  __ \                                  | |  |  \/  |                                  
 | |__) |_ _ ___ _____      _____  _ __ __| |  | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |  | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                          __/ |          
                                                                         |___/           
''')
print('-'*150)

#Generate the key for the first time only or else the program is gonna throw error saying that it has a invalid token because everytime you run the program it will generate a new key
'''key = Fernet.generate_key()
print(key)'''
key = (b'S2sTzn8xzwZKXTBKNIlYrj5lWMHzOqX6MlDJxc_MOwI=')
k = Fernet(key)

while True:
    username = input("Username:")
    passwd = str(getpass.getpass("Password:"))
    if username == "USERname" and passwd == "12345@pass":
        time.sleep(1)
        print("Login Confirmed!!")
        while True:
            time.sleep(1)
            user = input("Do you wanna ADD or VIEW? OR press Q to quit.\n-")
            if user.upper() == 'ADD':
                time.sleep(1)
                print("Please enter your username and passowrd you want to be added.")
                time.sleep(0.5)
                while True:
                    usrnm = input("Username:")
                    pwd = input("pwd:")
                    re_type = input('Re-Type your password:')
                    if pwd == re_type:
                        with open("keys.key", "a") as f:
                            f.write(f'{usrnm}|{k.encrypt(pwd.encode()).decode()}\n')
                        time.sleep(0.5)
                        print("Succesfully added.")
                        print('-'*150)
                        time.sleep(0.5)
                        add_more = input("Do you wanna add more? (Y/N)\n-")
                        if add_more.upper() == 'Y':
                            pass
                        else:
                            break
                    else:
                        print("Passwords doesnt match! Please try again!")
                        print("-"*150)
                        continue
            elif user.upper() == 'VIEW':
                time.sleep(1)
                with open('keys.key', 'r') as f:
                    for line in f.readlines():
                        data = line.rstrip()
                        us, passw = data.split('|') #since the split is '|', you need to work on something if your passowrd contains |
                        print("Username:", us, "| Password:", k.decrypt(passw.encode()).decode())
    

            elif user.upper()=='Q':
                exit()
            else:
                time.sleep(0.5)
                print('-'*155)
                print("Invalid Mode!")
                continue
    else:
        time.sleep(0.5)
        print("Wrong Credentials. Try Again!")
        print('-'*150)
        continue


