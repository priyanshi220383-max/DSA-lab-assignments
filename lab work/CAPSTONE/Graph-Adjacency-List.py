# ============================================
# SOCIAL NETWORK USING GRAPH
# ============================================

# Dictionary used as adjacency list
network = {}

# -------- ADD FRIENDSHIP --------
def add_friend(user1, user2):

    # Create empty friend lists if users not present
    if user1 not in network:
        network[user1] = []

    if user2 not in network:
        network[user2] = []

    # Add each other as friends
    network[user1].append(user2)
    network[user2].append(user1)

    print(user1, "and", user2, "are now friends")


# -------- REMOVE FRIENDSHIP --------
def remove_friend(user1, user2):

    if user2 in network[user1]:
        network[user1].remove(user2)

    if user1 in network[user2]:
        network[user2].remove(user1)

    print("Friendship removed")


# -------- GET FRIENDS --------
def get_friends(user):

    if user in network:
        print("Friends of", user, ":", network[user])
    else:
        print("User not found")


# -------- DEMO --------
add_friend("Aman", "Priya")
add_friend("Aman", "Rahul")
add_friend("Priya", "Sneha")

get_friends("Aman")

remove_friend("Aman", "Rahul")

get_friends("Aman")