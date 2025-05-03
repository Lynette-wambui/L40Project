# Simple Number Swap

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number"))
z, x, y = z, x, y

print("After swapping:")
print("First number:", z)
print("Second number:", x)
print("Third number:", y)





#String operations
name = "Skylerlyn"
age = 13
is_student = True
weight = 32.5

print("Name :", name)
print("Data Type of Name is", type(name))

print("Age :", age)
print("Data Type of Age is", type(age))

print("Is Student :", is_student)
print("Data Type of Is Student is", type(is_student))

print("Weight :", weight)
print("Data Type of Weight is", type(weight))


num1 = 550
num2 = 100

print("Number 1", num1)
print("Number 2", num2)

# Arithmetic Operators
print("Addition:", num1 + num2)
print("Subtraction:", num2 - num1)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Square root", num1**0.5)
print("Equal ?", num1==num2)
print("Number 1 greater?", num1>num2)
print("Number 2 greater?", num1<num2)


#String operations
first_name = "Western "
last_name = " Cosmetics"
full_name = first_name+last_name

word = 'Jambo!'*6

print("First Name :", first_name)
print("Last Name :", last_name)
print("Full Name :", full_name)
print("String Multiplied 5 times gives this result :", word)

word = 'Cosmetics'
print("Length of String :", len(word))
print("First Letter of String :", word[0])
print("Last Letter of String :", word[5])
print("String Sliced :", word[0:4])