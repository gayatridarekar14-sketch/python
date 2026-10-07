correct_password = 1234

for attempt in range (3):
  Password = int(input("enter the password:"))
if Password == correct_password:
    print("login successfull")
else:
    print("wrong password") 
