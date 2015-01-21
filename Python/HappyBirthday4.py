# PRbirthday4.py
# function examples
# uses main plus multiple functions with one parameter
# main is short
# prints the happy birthday song
# by Mrs. Redding

def main():
   sing("Jane")
   print()
   sing("Joe")
   print()
   
def sing(person):
   happy()
   happy()
   print("Happy birthday, dear", person + ".")
   happy()
   
def happy():
   print("Happy birthday to you!")
   
main()