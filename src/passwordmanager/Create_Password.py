#! /usr/bin/env python3.4

from random import random

class Create_Password:

   __lowercase = 'abcdefghijklmnopqrstuvwxyz'
   __uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   __numbers = '0123456789'
   __special = '!£$%^&<>?'
   __available = ''

   def __init__(self, has_lowercase, has_uppercase, has_numbers, has_special):
      if(has_lowercase):
         self.__available += self.__lowercase
      if(has_uppercase):
         self.__available += self.__uppercase 
      if(has_numbers):
         self.__available += self.__numbers
      if(has_special):
         self.__available += self.__special

   def random_charactors(self, length):
      password = ''
      j = 0
      
      for i in range (0, length):
         j = randint(0, len(self.__available))
         password += available[j, (j + 1)]
      
      return password

   def random_words(self, length):
      #Code to create a password of size length using random words from wordslist
      #Select a list of random sizes
      #Select a random word for each size
      return ''


