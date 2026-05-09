# ============================================
# FRIEND RECOMMENDATION SYSTEM
# ============================================

# User interests stored in dictionary
interests = {
    "Aman": ["Music", "Coding", "Gaming"],
    "Priya": ["Music", "Reading", "Coding"],
    "Rahul": ["Gaming", "Sports"],
    "Sneha": ["Coding", "Music"]
}

# -------- RECOMMEND FRIENDS --------
def recommend(user):

    scores = {}

    # Compare interests with all users
    for other_user in interests:

        if other_user != user:

            # Find common interests
            common = set(interests[user]) & set(interests[other_user])

            # Store count of common interests
            scores[other_user] = len(common)

    # Sort users by common interest count
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("Friend Recommendations:")

    for user, score in sorted_scores:
        print(user, "- Common Interests:", score)


# -------- DEMO --------
recommend("Aman")