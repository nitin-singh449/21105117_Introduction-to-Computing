print("Question 1")

sen = input("Please give an input- ") #taking input
sen=sen.lower().strip()
i=0

dict={}

#checking if the string input is a word or a sentence.
if " " not in sen:
     #searching for common elements
     while i<len(sen):
          counter=0
          k=0
          while k<len(sen):
               if sen[i]==sen[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1

          #storing the values in dictionary
          dict[f"{sen[i]}"]=counter
          i=i+1

else:
     #making a list of words using split method
     list = str.split(sen)
     #searching for common words
     while i<len(list):
          counter=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
                    #storing the pairs in dictionary
          dict[f"{list[i]}"]=counter
          i=i+1
#Printing the final result
print("Total occurances")
for key,value in dict.items():
    print(f"{key}-{value}")

                                #2nd Program


print("Question 2 ")


# Taking date from user.
date = int(input("Enter the date: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
print()

# Condition for valid dates.
check_1 = (month in (1,3,5,7,8,10,12) and (1 <= date <= 31))
check_2 = (month in (4,6,9,11) and (1 <= date <= 30))
check_3 = ((year % 4) == 0 and month == 2 and (1 <= date <= 29)) or ((year % 4) != 0 and month == 2 and (1 <= date <= 29))

# Calculating next date.
if (check_1 or check_2 or check_3) and (1800 <= year <= 2025): # checking whether date is valid or not. 
    
    # calculating next date for months having 31 days.
    if month in (1,3,5,7,8,10):
        if date < 31:
            date += 1
        else:
            date = 1
            month += 1

    # Calculating next date for month having 30 days.
    elif month in (4,6,9,11):
        if date < 30:
            date += 1
        else:
            date = 1
            month += 1

    # Calculating next date for feb because it have only 28 days.
    elif month == 2:

        # calculating next date in case of leap year.
        if year % 4 == 0:
            if date < 29:
                date += 1
            else:
                date = 1
                month += 1
        else:
            if date < 28:
                date += 1
            else:
                date = 1
                month += 1

    # Calculating next date for dec.
    else:
        if date < 31:
            date += 1
        else:
            date = 1
            month = 1
            year += 1
    
     # Printing next date.
    if date == 1 and month == 1 and year == 2026:
        print("Next date is out of range.")
    else:
        print(f"Next day is: {date}/{month}/{year}")

else:
    # printing if date is not valid.
    print("Invalid Date.")


                               #3rd Program


print("Question 3")

list_in = eval(input("Enter the list: "))
list_out = []
for i in list_in:
    list_out.append((i, i**2))                             #(i, i**2) is the tuple which is added in the list, i.e. list_out is list of tuples
print("Output:", list_out)


                               #4th Program


print("Question 4 ")

#given list
giv_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]

# prompting user for entering the grade.
grade_num = int(input("Enter the grade number: "))
print()

# checking grade is valid or not.
if 4 <= grade_num <= 10:

    # Printing the result depending upon the input grade.
    if grade_num == 10:
        print("Your grade is 'A+' and Outstanding Performance.")
    elif grade_num == 9:
        print("Your grade is 'A' and Excellent Performance.")
    elif grade_num == 8:
        print("Your grade is 'B+' and Very Good Performance.")
    elif grade_num == 7:
        print("Your grade is 'B' and Good Performance.")
    elif grade_num == 6:
        print("Your grade is 'C+' and Average Performance.")
    elif grade_num == 5:
        print("Your grade is 'C' and Below Average Performance.")
    else:
        print("Your grade is 'D' and Poor Performance.")

else:

    # Printing the error msg if grade is invalid.
    print("Invalid grade.")

                              #5th Program


print("Question 5")

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end= "")
            counter=counter+1
        column=column+1
    print("")


                              #6th Program

print("Question 6")

condition=True

#Defining dictionary to store the values
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        Sid=int(input("Please Enter SID of Student- "))
        name=input("Please enter the name of the Student- ")
        Dictionary[Sid]=name
        prompt= input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False

print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part d")
Sid_tbf=int(input("Please enter the student's SID whose detail you need- "))
if Sid_tbf in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[Sid_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")


                              #7th Program


#print("Question 7 ")

x = 0
y = 1
sum = 0
while True:                                                                                                         
    num = int(input("Enter the no. of terms : "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
        continue
    if num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else:
        print("The Fibonacci sequence is as follows:")
        print(x,end=" ")
        for i in range(1,num):
            sum += y
            print(y, end=" ")
            z = x + y
            x = y
            y = z
        print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (num,sum/num))
        break


                              #8th Program


print("Question 8 ")
   
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

print("Part a")
print("Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)

print("Part b")
print("Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)

print("Part c")
print("Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)

print("Part d")
print("Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)

print("Part e")
print("Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)
