#!/usr/bin/python
# 11/21/19
# Recursion done in python
# Author: Lu





def main():

  recursion()

  countdownBase(9)

  fact(3)

def recursion():

  print ("This is Recursion in python")


#def countdown(i):
#  print ("This will loop forever")
#  print i
#  countdown(i-1)

def countdownBase(i):
  print i

  if i<= 0:

    return

  else:
    countdownBase(i-1)

def fact(i):

  if i == 1:

    return 1

  else:

    return i * fact(i-1)

main()
