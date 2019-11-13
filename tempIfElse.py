#function to check heat

def main():
    celsius = float(input("what is the Celsius Temperature?"))
    fahrenheit = 9/5 * celsius + 32
    print("the temperature is", fahrenheit, "degrees fahrenheit.")
    if fahrenheit >= 90:
        print ("It's really hot out there, be careful!")
    if fahrenheit <= 30:
        print("brr. be sure to dress warm")

main()
