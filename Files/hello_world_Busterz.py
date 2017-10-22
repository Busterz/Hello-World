# LANGUAGE: Python 3
# AUTHOR: Deddy T
# GITHUB: https://github.com/Busterz

user = input("Hi there, what's your name? ")
if len(user) > 0:
  user = user[0].upper() + user[1:]
print ("Hello %s!") % user
print ("Hello World!")
print ("Welcome to Programming!")
