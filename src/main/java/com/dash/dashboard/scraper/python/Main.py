from login import Vula
from sites import Site

print("Hi!")

studentNumber = input("Please enter your UCT Student Number: ")

password = input("Please enter password: ")

vula = Vula(studentNumber, password)

try:
    print("logging in...")
    sites = Site(vula.login())
    print("You are now logged in")
    print()
    print("Gathering your data...")
    sites.scrape()
    print("Done!!!")
except:
    print("Failed to login!!")
    print("Please check your internet connection and try again!")

