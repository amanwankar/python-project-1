# SIMPLE AREA CALCULATOR 

print("welcome to the simple Area calculator")

shape = input("Enter 'S' for squre or  'R' for rectangle : ")

if shape == 'S':
  print("\n Calculating the Area of Squre")
  length = float(input("Enter the length of one side of Squre : "))
  area_squre = length**2
  print("Area of Squre is :",area_squre)

elif shape == 'R':
  print("\n so you want to calculate rectangle ")
  len_rectangle = float(input("Enter the the length of Rectangle : "))
  wid_rectangle = float(input("Enter the the width of Rectangle : "))
  area_rectangle = len_rectangle * wid_rectangle
  print("the Area of Rectangle is : ",area_rectangle)

else:
  print("Invalid input .please Enter 's' or 'r' .")
