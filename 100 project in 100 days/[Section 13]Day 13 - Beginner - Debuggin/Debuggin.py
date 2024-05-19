"""
In this one there will be different scripts where there are errors, typos, bugs etc and beneath i will also have the answers
"""
#----------------#
#Example Number 1
#----------------#
#number = int(input()) # Which number do you want to check?

#if number % 2 = 0:
#  print("This is an even number.")
#else:
#  print("This is an odd number.")

#----------------#
#Solution Number 1
#----------------#
#number = int(input()) # Which number do you want to check?

#if number % 2 == 0:
#  print("This is an even number.")
#else:
#  print("This is an odd number.")

# Which year do you want to check?
year = input()

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  