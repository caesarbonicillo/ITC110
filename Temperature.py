#convert Celsius to Fehrenheit

def main(): #this is a function
    #input
    celsius = eval (input ("Enter the temp in Celsius ")) #must convert to number call function EVAL
    #processing
    fahrenheit = round(9/5 * celsius + 32, 0)
    #output
    print (celsius, "The Fehrenheit temp is", fahrenheit)

main() # press f5 to run

def kiloMile():
    kilo = eval (input("enter kilometers "))
    miles = 1.6 * kilo
    print ( kilo, "The conversion is", miles) 

kiloMile()
