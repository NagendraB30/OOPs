class Session:
    def __init__(self, user):
        self.user = user
        print(f"Session started for {self.user}")

    def __del__(self):
        print("Session Ended")

s1 = Session("Admin")

del s1