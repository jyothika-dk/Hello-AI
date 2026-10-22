import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Workout & motivational data
workout_types = {
    "cardio": ["Running", "HIIT Circuit", "Jump Rope"],
    "strength": ["Weightlifting", "Resistance Bands", "Bodyweight Calisthenics"],
    "flexibility": ["Yoga", "Dynamic Stretching", "Pilates"]
}

quotes = [
    "Why do weightlifters make great programmers? They know how to handle heavy lifting!",
    "Why did the smartphone go to the gym? It wanted to improve its core processing!",
    "Why do fitness enthusiasts always look cool? Because of all their heavy lifting fans!"
]

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide workout recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "FitBot: Cardio, strength, or flexibility?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in workout_types:
        suggestion = random.choice(workout_types[preference])
        print(Fore.GREEN + f"FitBot: How about {suggestion}?")
        print(Fore.CYAN + "FitBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"FitBot: Awesome! Smash that {suggestion} workout!")
        elif answer == "no":
            print(Fore.RED + "FitBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "FitBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "FitBot: Sorry, I don't have that type of workout.")
        recommend()

# Offer gear tips based on user's workout type and duration
def gear_tips():
    print(Fore.CYAN + "FitBot: What workout are you planning?")
    activity = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "FitBot: How many minutes long is your session?")
    duration = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"FitBot: Gear tips for your {duration}-minute {activity} session:")
    print(Fore.GREEN + "- Wear breathable, moisture-wicking clothing.")
    print(Fore.GREEN + "- Bring a water bottle to stay hydrated.")
    print(Fore.GREEN + "- Don't skip your warm-up and cool-down.")

# Tell a random fitness joke/quote
def tell_joke():
    print(Fore.YELLOW + f"FitBot: {random.choice(quotes)}")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest workouts (say 'recommendation')")
    print(Fore.GREEN + "- Offer gear tips (say 'gear')")
    print(Fore.GREEN + "- Tell a fitness joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm FitBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "gear" in user_input or "packing" in user_input:
            gear_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "FitBot: Stay active! Goodbye!")
            break
        else:
            print(Fore.RED + "FitBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()