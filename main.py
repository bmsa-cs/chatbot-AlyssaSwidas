"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")

n = input("What is your name:")
print ("Hi" + " " + n)
if n == "alyssa":
    print ("My name is also alyssa")
elif n == "aly":
    print ("That is my nickname")
else:
    print ("My name is Alyssa")


print("Here is a positivity quote")

x = random.randint(1,5)
if x == 1:
    print("Sharing is Caring")
elif x == 2:
    print ("Love yourself")
elif x == 3:
    print("You are Enough")
elif x == 4:
    print ("You are Worthy")
elif x == 5:
    print ("Live Every Day to the Fullest")

  
m = input("What would you say your current mood is?")
if m == "happy":
    print ("That is good to hear")
elif m == "ok":
    print ("Are you sure I say im ok all the time when im not")
else:
    print ("It's okay everyone has off days")
 
a = int(input("How many siblings do you have? "))
if s == 5:
    print(" I have five siblings to")
elif s == 0:
    print (" So your an only child thats cool ")
else:
    print (" I have multiple siblings too ")

c = input("What is your favorite color?")
if c == "blue":
    print("That is also my favorite color")
else:
    print("That is a pretty color")
  
s = input("Do you play any sports")
if s == " yes":
    print (" Thats cool ")
elif s == "no":
    print ("Thats okay you don't have to") 
else:
    print (" I play softball ")



if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()