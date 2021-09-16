# Zadania_python

Module 4

1.Task: Palindromes

definition palindrome

def palindrome(word):

Checks if passed argument is a palindrome i.e. a word, number or phrase, which reads the same backward as forward, such as madam or abba.
If passed argument is a palindorme, returns Boolean value True.
Else, returns Boolean value False.
Arguments:
    word

2. Task: Calculator

definition calculator

def calculator(operation, number1, number2):
It's a calculator that takes two numbers to calculate, based on arguments passed. He can add, subtract, multiply and divide.
Arguments:
    operation (+,-,* or /)
    number1
    number2

Module 7
 1. Task: Cards
 
 class BaseContact
    def __init__(self, first_name, last_name, private_phone,email)
 Arguments:
 first_name, 
 last_name, 
 private_phone,
 email
 
 BaseContact subclass
 class BusinessContact(BaseContact):
    def __init__(self, position, company_name, business_phone, *args, **kwargs)
    
 Arguments:
 first_name, 
 last_name, 
 private_phone,
 email
 position, 
 company_name, 
 business_phone
 
 definition create_contacts 
 def create_contacts(card_type, quantity):
 It creates the lists of contacts based on arguments passsed. Card type can be either "BaseContact" relating to class BaseContact or "BusinessContact" relating to class "BusinessContact". 
  Arguments:
  card_type,
  quantity
