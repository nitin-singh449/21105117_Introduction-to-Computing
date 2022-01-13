

             #1st Program
print(       "Program 1 " )          
numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))
numb3 = int(input("Enter third number: "))

avg = (numb1+numb2+numb3)/3

print("Average of numbers is: ",avg)      




              #2nd Program
#constants
rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000

#Taking input from the user
gross_income = float(input("\nEnter your gross income : "))
number_of_dependents = int(input("Enter number of dependents : "))

#Calculation of tax 
taxable_income = round(gross_income-standard_deduction-(dependent_deduction*number_of_dependents), 1)
tax = taxable_income*rate


print("Tax to be paid is $",tax,"\n")





              #3rd Program

print("                     3rd program")

sid=int(input("enter the sid= "))
name=input("enter the name= ")
gender=input("enter the gender F/M =")
branch=input("enter the branch name =")
cgpa=float(input("enter the cgpa= "))
student=[sid,name,gender,branch,cgpa]

print("Student: ",student)





              #4th Program

print("                      4th program")

mk1= float(input("enter the marks of 1st student= "))
mk2= float(input("enter the marks of 2nd student= "))
mk3= float(input("enter the marks of 3rd student= "))
mk4= float(input("enter the marks of 4th student= "))       
mk5= float(input("enter the marks of 5th student= "))

marks =[mk1,mk2,mk3,mk4,mk5]
marks.sort()
print(marks)

      



              #5th Program


print("                       5th program")

color=['Red','Green','White','Black','Pink','Yellow']
COLOR1=[]
COLOR1.extend(color)
print("ORIGINAL LIST:",COLOR1)
COLOR1.pop(3)
print("List after removing 4th color: ",COLOR1)
color[3:5]=['Purple']
print("List after replacing black and pink by purple: ",color)

