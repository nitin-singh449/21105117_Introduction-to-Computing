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

year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

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
while True:                                                                                                         #loop for making sure the user inputs the value between 4 and 10
    grade = eval(input("Enter the grade point of the student: "))
    if 4 <= grade <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in giv_table:                                                                                               #i is for iterating through the lists in the list and j is for iterating through the elements of each list
    for j in i:
        if j == int(grade):
            print("Your Grade is '%s' and %s Performance" % (i[0],i[1]))

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
