#  CALCULATOR USING SIMPLE CONCEPT

# ......concept we used in here is print(),Aramathic operation.......
print("WELCOME TO SIMPPLE CALCULATOR")
print(("-"+"*")*20)

# ....here we use the concept of variable ,typecasting and float.......

num1 = float(input("Enter your frist digit :"))
operators = input("Enter your operator ex :-(+,-,*,/,) : ")
num2 = float(input("Enter your second digit :"))

result = 0
# .....here we simply use the the concept of else if and if statment.....

if operators == "+":
  result = num1 + num2

elif operators == "-":
  result = num1 - num2

elif operators == "*":
  result = num1 * num2

elif operators == "/":
  result = num1 / num2

else:
  print("Enter valid details or check the operation ")
  
print("Your  reasult is :",result)  

