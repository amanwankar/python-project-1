# Simple grader

print("....simple Student grader....")

marks = input("Enter your marks between (1-100) : ")

markes = int(marks)

grade = ""

if markes >= 90:
  grade = 'A'

elif markes >= 80 :
  grade = 'B'  

elif markes >=70:
  grade = 'c'  

elif markes >=60:
  grade = 'D'  

else:
  grade = 'F'  

print("with score of ",(markes),"your grade is",[grade])  