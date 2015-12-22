#! /usr/bin/env python3.4


class Account_Information:

   __password = ''
   __account = ''
   __description = ''

   def __init__(self, password, account, description):
      self.__password = password
      self.__account = account
      self.__description = description

   def to_string(self):
      return 'Password: ' + self.__password + '\nAccount: ' + self.__account + '\nDescription: ' + self.__description


