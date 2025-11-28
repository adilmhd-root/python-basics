username = "admin"
password = "1234"

u = input("enter username: ")
p = input("enter password: ")

if u == username and p == password:
    print("login successful")
else:
    print("login failed")