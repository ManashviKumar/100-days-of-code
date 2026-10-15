
# constructor is a part of blueprint which tell us what should happen when
# object is being constructed.
# It is also known as initializing object,when the object is being initialized.
# we can set variables or counters to their starting values.
# we can create constructor using special function "def__init__(self)"
# It is used to initialize attributes
# each time we use User() data inside "init" will triggered/run


class User:
    def __init__(self,user_id,username):
        self.id = user_id #self is use to create new attribute
        self.username = username
        self.followers = 0 #here follower is set to 0 as default
        self.following = 0
    def follow(self,user):
        self.followers += 1
        self.following = 1

user_1 = User("001","Manash")
user_2 = User("002","Kumar")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
