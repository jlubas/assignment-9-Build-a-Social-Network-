class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]

            # Create bidirectional friendship
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            print("Friendship not created. One or both people don't exist!")

    def print_network(self):
        for name, person in self.people.items():
            # List the names of each person's friends
            friend_names = [friend.name for friend in person.friends]

            # Join names with a comma
            friends = ", ".join(friend_names)
            print(f"{name} is friends with: {friends}")




# Test your code here


alex = Person("Alex")
jordan = Person("Jordan")

print(alex.friends)  # []
alex.add_friend(jordan)
print(alex.friends[0].name)  # Jordan

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
print(network.people)

network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()

# Test duplicate people
network.add_person("Alex")
print("Total people after adding Alex again:", len(network.people))


# Design Memo Reflection 

# Why is a graph the right structure to represent a social network?

    # I think a graph is a good choice for a social network because people can have many friends, and everyone can be connected in different ways. 
    # A graph uses nodes to represent people and edges to show their friendships. For example, Alex can be friends with Jordan, Morgan, and Taylor at the same time. 
    # These friendships work both ways, so if Alex is friends with Jordan, Jordan is also friends with Alex. Using an adjacency list helped me organize these connections.

# Why wouldn’t a list or tree work as well for this?

    # A simple list of names would not work as well because it does not show who is friends with whom unless we add more information
    # A tree is also different because it has a starting point, called a root, with branches underneath it. In a social network, nobody needs to be at the top. 
    # People can have different friends without following a specific order. This is why a graph makes more sense to me.

# What performance or structural trade-offs did you notice when adding friends or printing the network?

    # While working on my code, I found it interesting how the dictionary stores each person by name, while the friends list keeps track of their connections. 
    # Adding friends was simple, but the program had to check whether someone was already on the list to avoid duplicates. 
    # This could take longer if a person had hundreds of friends. Printing the network was also easy to understand because the program went through each person and displayed their friends. 
    # However, a larger network would take more time to print.

# Overall, this project helped me see how graphs can represent friendships in real life.