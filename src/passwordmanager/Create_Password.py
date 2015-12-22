#! /usr/bin/env python3.4

class Create_Password:

   __lowercase = 'abcdefghijklmnopqrstuvwxyz'
   __uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   __numbers = '0123456789'
   __special = '!£$%^&<>?'
   __available = ''

   def __init__(self, has_lowercase, has_uppercase, has_numbers, has_special):
      if(has_lowercase):
         self.__available = self.__available + self.__lowercase
      if(has_uppercase):
         self.__available = self.__available + self.__uppercase 
      if(has_numbers):
         self.__available = self.__available + self.__numbers
      if(has_special):
         self.__available = self.__available + self.__special

   def random_charactors(self, length):
      #Code to create a password of size length using random charactors from available
      return ''

   def random_words(self, length):
      #Code to create a password of size length using random words from wordslist
      return ''


