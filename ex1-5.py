
"""
Exercise 1:  Mailing Address
Create a program that displays your name and complete mailing 
address formatted in the manner that you would usually see it 
on the outside of an envelope.  Your program does not need to 
read any input from the user.  (9 lines)
"""
print("\nVictoria Louis \n8630 S Cove Dr \nMaineville, OH 45039")
"""
Exercise 2:  Hello
Write a program that asks the user to enter his or her name.  
The program should respond with a message that says hello to 
the user, using his or her name.  (9 lines)
"""
print("Please enter your name: ")
name=input()
print("Hello", name,"!")
"""
Exercise 3:  Area of a Room
Write a program that asks the user to enter the width and 
length or a room.  Once the values have been read, your 
program should compute and display the area of the room.  
The length and the width will be entered as floating point 
numbers.  Include units in your prompt and output message;  
either feet or meters, depending on which unit you are more 
comfortable working with.  (13 lines)
"""
print("Please enter the width of the room:")
width=input(int)
print("Please enter the length of the room:")
length=input(int)
area=width*length
print=(area " square feet")
"""
Exercise 4:  Area of a Field
Create a program that reads the length and width of a 
farmer’s field from the user in feet.  Display the 
area of the field in acres.  
Hint: There are 43,560 square feet in an acre
"""
print("Please enter the width of the field in feet:")
width=input(int)
print("Please enter the length of the field in feet:")
length=input(int)
area=width*length
acres=area/43560
print=(acres " acres")
"""
Exercise 5:  Bottle Deposits
In many jurisdictions a small deposit is added to drink 
containers to encourage people to recycle them.  In one 
particular jurisdiction, drink containers holding one liter 
or less have a $0.10 deposit, and drink containers holding 
more than one liter have $0.25 deposit.
Write a program that reads the number of containers of each 
size from the user.  Your program should continue by computing 
and displaying the refund that will be received for returning 
those containers.  Format the output so that it includes a dollar 
sign and always displays exactly two decimal places.  (15 lines)
"""
()

def bottleDeposits():
    # reads the number of bottles
    numOneLiterBottle = int(input("Number of 1L bottles: "))
    numMoreOneLiterBottle = int(input("Number of more than 1L bottles: "))
    refund = numMoreOneLiterBottle*0.25+numOneLiterBottle*0.1
    refund = round(refund, 2)
    print("Your refund will be: $", "{:.2f}".format(refund))
    # adding everything greater than 1


    # To ensure we have two decimal places
    # number_two_decimal = "{:.2f}".format(number_string)
    # print(number_two_decimal)

bottleDeposits()
#Testing Suite
#areaRoom()
