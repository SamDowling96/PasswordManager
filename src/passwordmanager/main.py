#!/usr/bin/env python3.4

from Account_Information import *
from Create_Password import *


def main():
   title('* Password Manager *')
 
   choice = option_selection()

   password = get_password(choice)
   account = raw_input('Enter in Account: ')
   description = raw_input('Enter in Description: ')

   info = Account_Information(password, account, description)

   print
   print(info.to_string()) 

def title(title):
   print
   print('*' * len(title))
   print(title)
   print('*' * len(title))
   print

def option_selection():
   create_password = Create_Password(True, False, False, False)
   
   choice = input('Select an option:\n\n' + 
                  '\t(1)Enter it yourself\n' + 
                  '\t(2)Generate by random charactors\n' +
                  '\t(3)Generate by random words\n\n' + 
                  'Option(1, 2, 3 or quit())? ')
   return choice

def get_password(choice):   
   print
   if choice == 1:
      password = raw_input('Enter in password: ')
   elif choice == 2:
      length = int(input('Enter in length: '))
      password = create_password.random_charactors(length)
   elif choice == 3:
      length = int(input('Enter in length: '))
      password = create_password.random_charactors(length)
   else:
      print('\nError: Invalid option \nPlease try again\n')
      option_selection()
   
   return password


if __name__=='__main__':
   main()


