                                 #1st Program

print(“Question1”)

print('Question1')

input_string = 'Python is a case sensitive language'

# printing the length of input_string.
print("\n (a)")
print(f"Length of Input String = {len(input_string)}")

# printing the input_string in reverse order.
print("\n (b)")
print(input_string[::-1])


# slicing and printing the input_string.
print("\n (c)")
sliced_string = input_string[10:26]
print(sliced_string)


# replacing and printing.
print("\n (d)")
new_string = input_string.replace("a case sensitive", "object oriented")
print(new_string)


# printing index of "a" from input_string.
print("\n (e)")
print(input_string.index("a"))


# replacing blank white spaces with empty string.
print("\n (f)")
print(input_string.replace(" ", ""))



                                #2nd Program

print("Question 2\n")


Name = "Nitin Singh"
SID = "21105117"
Department = "ECE"
CGPA = "10"


print(f"Hey, {Name.title()} here! \nMy SID is {SID} \nI am from {Department} and my CGPA is {CGPA}")

                                

                                

                                #3rd Program


print("Question 3")


a = 56
b = 10

print(" a&b is : ", a & b)
print(" a|b is : ", a | b)
print(" a^b  is : ", a ^ b)

# Left shifting both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)

# Right shifting a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)


        
                                #4th Program


print("Question 4")

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number  : "))

#finding the highest no.
if a > b:
    if a > c:
        highest_number = a
    else:
        highest_number = c

if b > a:
    if b > c:
        highest_number = b
    else:
        highest_number = c


print(f"The Highest number is = {highest_number}")



                                #5th Program


print("Qustion 5")

input_string = input("Enter input string : ")

if "name" in input_string:
    print("Yes")
else:
    print("No")


                                #6th Program


print("Question 6\n")

a = int(input("Enter 1st length : ")) 
b = int(input("Enter 2nd length : "))
c = int(input("Enter 3rd length : "))

# checking conditions

if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")
