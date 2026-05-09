# ============================================
# PROFILES USING HASHING + LISTS
# ============================================

# Dictionary used as hash table
profiles = {}

# -------- ADD USER --------
def add_user(username, age, city):

    # Store user data in dictionary
    profiles[username] = {
        "age": age,
        "city": city
    }

    print(username, "added successfully")


# -------- GET PROFILE --------
def get_profile(username):

    # Check if user exists
    if username in profiles:
        print(profiles[username])
    else:
        print("User not found")


# -------- UPDATE PROFILE --------
def update_profile(username, age, city):

    if username in profiles:

        # Update values
        profiles[username]["age"] = age
        profiles[username]["city"] = city

        print(username, "updated successfully")

    else:
        print("User not found")


# -------- DEMO --------
add_user("Aman", 20, "Delhi")
add_user("Priya", 21, "Mumbai")

get_profile("Aman")

update_profile("Aman", 22, "Noida")

get_profile("Aman")