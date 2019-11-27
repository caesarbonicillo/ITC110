person = ("kevin, james john, bill")
person = person.split(",")
print(person)

def happy():
    print("Happy birthday to you")

def sing(person):
    happy()
    happy()
    print("Happy Birthday, dear", person + "!")
    happy()

sing("david")

def main():
    sing("david")
    print() #gives it one space between verses.
    sing("mark")
    print()
    sing("susan")
    print()
    sing(person[1])
main()
