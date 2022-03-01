                                  #Program 1
print("Question 1")

num = 0
def towerofhanoi(n, initial_rod, final_rod, extra_rod):
    global num
    if n == 0:                                                                                          #Base case
        return
    num += 1
    towerofhanoi(n-1, initial_rod, extra_rod, final_rod)                           #Recursive call
    print("Move disk",n,"from rod",initial_rod,"to rod",final_rod)
    towerofhanoi(n-1, extra_rod, final_rod, initial_rod)

no_of_discs = int(input("Number of discs: "))
print("\nA is the initial rod\nB is the extra rod\nC is the final rod\n\nSteps:")
towerofhanoi(no_of_discs, 'A', 'C', 'B')
print("\nNumber of steps will be: %d" % (num))



                                  #Program 2


print("Question 2")

#Entering rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

print("Using Recursion: ")

def pascal(n, orgnum=n):
    if n == 0:
        return

    pascal(n - 1, orgnum)

    # printing the spaces
    print('  ' * (orgnum - n), end='')

    # first number is always 1
    entry = 1
    for i in range(1, n + 1):
        print(entry, end='   ')

        # using Binomial Coefficient
        entry = entry * (n - i) // i
    print()


pascal(n)

# using iteration
print("\nUsing loops:\n")
for line in range(1, n + 1):

    print('  ' * (n - line), end='')

    x = 1
    for i in range(1, line + 1):
        print(x, end='   ')

        x = x * (line - i) // i
    print()


                                  #Program 3


print("Question 3")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# ensuring that denominator is not zero
while b == 0:
    b = int(input("Denominator cannot be zero. Please enter a non zero number : "))

Q, R = divmod(a, b)
m = [Q, R]


def division():
    Q, R = divmod(a, b)
    print(f"Questiont:{Q}\nRemainder:{R}")


division()

print('a)')
print(callable(division))

print('b)')
if all(divmod(a, b)):
    print('All the values are non zero')
else:
    print('All the values are not non zero')

print('c)')
m.extend([4, 5, 6])
print("After adding 4,5,6 : ", m)
filtered = filter(lambda n: n > 4, m)
print("Values greater than 4 are : ", list(filtered))

print('d)')
s = set(m)
print(s)

print('e)')
f_s = frozenset(s)
print("Immutable set : ", f_s)

print('f)')
m = max(f_s)
print(hash(str(m)))


                                  #Program 4

print("Question 4")


class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object destroyed")


# assigning values
student1 = Student("Nitin Singh", 21105117)
print("Object is created ")

# printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

# deleting object
del student1


                                  #Program 5

print("Question 5")


class Employees:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def record(self):
        print("Employee Name : ", self.name.title())
        print("Employee Salary : ", self.salary)
        

e1 = Employees("Mehak", 40000)
e2 = Employees("Ashok", 50000)
e3 = Employees("Viren", 60000)


print("Record of all employees\n")
e1.record()
e2.record()
e3.record()


print("(a)")
print("Updated record of Mehak:")
e1.Salary = 70000
e1.record()

print("(b)")
del e3
print("Record of Vivek deleted")


                                  #Program 6

print("Question 6")

def friendship(W1, W2):

    W1 = W1.lower()
    W2 = W2.lower()

    # checking whether all the letters are same in both words
    if sorted(W1) == sorted(W2):
        print("Your friendship is real")
    else:
        print("Your friendship is fake")

wd1 = input("Friend 1, please enter your word : ")
wd2 = input("Friend 2, please enter your word : ")


#Input from shopkeeper
a=input("Is the new word meaningful?(Y/N) : ")

if a.upper()=="N":
    print("Your friendship is fake.")
elif a.upper()=="Y":
    friendship(wd1, wd2)
else:
    ("Error!")
