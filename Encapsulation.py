class InstagramAccount:
    def __init__(self, name, password):
        self.account_name = name 
        
        self._private_reels = [] 
        
        self.__archived_reels = [] 
        
        self.__password = password 

    
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Added to Private Reels: {reel_name}")

    def display_private_reels(self, is_follower):
        if is_follower == True:
            print(f"Private Reels: {self._private_reels}")
        else:
            print("Access Denied! Only followers can view private reels")


    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Added to Archived Reels: {reel_name}")

    def display_archived_reels(self, password_input):
        if password_input == self.__password:
            print(f"Archived Reels: {self.__archived_reels}")
        else:
            print("Access Denied! Wrong password.")


    def get_archived_reels(self, password_input):
        if password_input == self.__password:
            return self.__archived_reels
        else:
            return "Wrong Password"

    def set_password(self, new_password):
        self.__password = new_password
        print("Password updated successfully!")



my_insta = InstagramAccount("Nagendra_B", "1234") 

my_insta.add_private_reel("Party Video") 
my_insta.add_archived_reel("Secret Vlog") 

print("--- Testing Private Reels ---")
my_insta.display_private_reels(False) 
my_insta.display_private_reels(True) 

print("\n--- Testing Archived Reels ---")
my_insta.display_archived_reels("0000") 
my_insta.display_archived_reels("1234") 

print("\n--- Updating Password ---")
my_insta.set_password("5678") 
my_insta.display_archived_reels("5678")