def login_check(func):
    def wrapper(user, password):
        if user == "admin" and password == "1234":
            print("Login successful")
            func(user, password)
        else:
            print("Access Denied / Login failed")
    return wrapper

@login_check
def dashboard(user, password):
    print("Welcome to the admin dashboard!")

dashboard("admin", "1234")  
dashboard("user", "wrong")  