myString = input("Enter the string you want to convert to ASCII > ")

def convert(myString):
    counter = 0
    myList = []
    for x in str(myString):
        counter += int(ord(x))
        myList.append(ord(x))
        print(ord(x), end=" ")
    print("\nSum: " + str(counter))
    print(myList)


convert(myString)