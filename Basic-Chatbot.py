# Greet the user
print("Welcome aboard! I am your Study Companion. What is your name? : ")

# Get user input
name = input()

# Respond to the user's name
print(f"Great to have you here, {name}!")

# Ask a question
print("Do you prefer studying during the day or at night? (day/night) : ")
time_preference = input().lower()

# Use conditional statements to respond based on input
if time_preference == "day":
    print("Early bird catches the worm! Daylight can really help with focus.")
elif time_preference == "night":
    print("A night owl! The quiet hours are often best for deep concentration.")
else:
    print("Interesting! You must adapt your study routine depending on the situation.")

# End the conversation
print(f"Thanks for sharing, {name}. Happy studying and goodbye!")