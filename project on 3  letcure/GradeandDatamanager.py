# PROGRAMM OF GRADE AND DATA MANAGER

Student_record = [
  ["Aman",98,'A',"Computer Engineer"],
  ["yash",78,'B',"EXTC Engineer"],
  ["harshal",88,'C',"civil Engineer"],
  ["laukit",98,'A',"mechinical Engineer"],
  ["prathemesh",75,'C',"AIDS Engineer"],
  ["om",77,'C',"civil Engineer"],
  ["samar",83,'B',"Computer Engineer"],
  ["soham",88,'A',"Computer Engineer"]
,
]

cource_info = ("Data structure",5,"Credits",2025)
print("Sudent Reacords : ",Student_record)

#  it give course becouse of this  [3] = computer engineering
aman = Student_record[0][3]
print("Aman Course : ",aman)

# UPDATE THE NAME TO AMAN WANKAR
Student_record[0][0] = "Aman wankar"
print("Updated Name : ",Student_record[0][0])

# GIVE 3 STUDENET FROM TOP
Top_student = Student_record[:3]
print("top 3 sudent",Top_student)

# THREE STUDENT FROM BOTTEM
Last_two = Student_record[-2:]
print("Last two student is ; ",Last_two)

# APPEND THE LIST WITH THIS NAME AND ADD AT THE BUTTOM
Student_record.append(["Abhishake",68,'A',"AI tech"])
print("updated list is : ",Student_record)

# NAME GOES TO ASSINDING ORDER 
Student_record.sort()
print("After short Assending name is :",Student_record)

# LIST GOES TO DECENDING ORDER
Student_record.sort(reverse=True)
print("After short (reverae = True) Assending name is :",Student_record)

# IT WILL RREVERSE THE STRING THE STRING
Student_record.reverse()
print("enter the reverse form",Student_record)

# IT WILL ADD THIS NAME TO LIST
Student_record.insert(1,["kirti wankar",88,"c","compture engineer"])
print("your insert value is : ",Student_record)


# TUPLE EXAMPLE

grade_tuple = ("A","B","C","A","A")
# COUNT THE THE 'A' IN STRING
count = grade_tuple.count("A")
print("your count is :",count)

# FIND THE STRING NUMBER OF 'B'
index= grade_tuple.index("B")
print("your index is  : ",index)