#  USERNAME VALIDATOR

print("........... USERNAME VALIDATOR..........")
print("username must be more then 5 letter and contaoin no space.")

username = input("please Enter your Username :")
username_length = len(username)
space = username.find(" ")

if username_length  < 5:
  print("validetion faild enter more then 5 letter . ")

elif space != -1:
  print("validetion faild username does not contain any spaces . ")  

else:
  print("succcess ! welcome to our app",username.capitalize())

  count = username.count("a")
  print("fun fact your username has 'a' letter in your username") 