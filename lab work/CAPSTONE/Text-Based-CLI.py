# ============================================
# SIMPLE TEXT-BASED CLI
# ============================================

profiles = {}

while True:

    print("\n1. Add User")
    print("2. View User")
    print("3. Exit")

    choice = input("Enter choice: ")

    # -------- ADD USER --------
    if choice == "1":

        name = input("Enter name: ")
        age = input("Enter age: ")

        profiles[name] = age

        print("User added successfully")

    # -------- VIEW USER --------
    elif choice == "2":

        name = input("Enter name: ")

        if name in profiles:
            print("Age:", profiles[name])
        else:
            print("User not found")

    # -------- EXIT --------
    elif choice == "3":

        print("Program Ended")
        break

    else:
        print("Invalid choice")