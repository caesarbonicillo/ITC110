#quadratic quations must be a positive number

import math

def main():
    print("this program finds real solutions to quadratic equations")

    a = float(input("enter a coefficient a:"))
    b = float(input("enter coefficient b:"))
    c = float(input("enter coefficient c:"))
    #run only if code is greater or qual to zero
    discrim = b * b - 4 * a *c
    if(discrim < 0): #1, 2, 3
        print("no real roots") # should always put the default in before any real work that way it doesn't do any unnessesary work.
    elif(discrim ==0):#1, 2, 1
        root = -b / (2 * a)
        print("there is a double root at", root)
    else:#1, 5, 6
        discRoot = math.sqrt(b * b -4 *a *c)
        root1 = (-b + discRoot) / (2* a) 
        root2 = (-b - discRoot) / (2 * a)
        print ("\nThe solutions are:", root1, root2)
        
main()
