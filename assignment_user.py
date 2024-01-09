class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
# display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
# Have this method change the user's member status to True and set their gold card points to 200. 
# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member."
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User already a member")
        return self
# Have this method decrease the user's points by the amount specified. 
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("You don't have enough points.")
        return self

user_simon = User("Simon", "Oliver", "simon@email.com", 26)

user_simon.display_info().enroll().spend_points(50).display_info().enroll().spend_points(250)
