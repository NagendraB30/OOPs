class User:
    def __new__(cls, name):
        print("1. Object is being created (Memory Allocated)")
        return super().__new__(cls)

    def __init__(self, name):
        print("2. Object is initialized (Variables Set)")
        self.name = name

u1 = User("Nagendra")