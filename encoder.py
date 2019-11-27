def main():
    print("this program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message \n")
    message = input ("please enter the mesage to code")

    print("\nHere are the Unicode codes:")

    for ch in message:
         print (ord(ch), end=" ")
    
    
main()




