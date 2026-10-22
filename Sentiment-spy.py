import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Emojis for the start of the program
print(f"{Fore.CYAN} 🍳 Welcome to Chef's Recipe Critic! 🍳{Style.RESET_ALL}")

chef_name = input(f"{Fore.MAGENTA}Please enter your name, Chef: {Style.RESET_ALL}").strip()
if not chef_name:
    chef_name = "Master Chef"  # Fallback if user doesn't provide a name

# Store recipe reviews as a list of tuples: (text, polarity, rating_type)
recipe_history = []

print(f"\n{Fore.CYAN}Greetings, Chef {chef_name}!")
print(f"Type a food review or dish description and I will evaluate it using TextBlob.")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, "
    f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a valid review or command.{Style.RESET_ALL}")
        continue

    # Check for commands
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Closing the kitchen. Farewell, Chef {chef_name}! 🍽️{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        recipe_history.clear()
        print(f"{Fore.CYAN} Kitchen log cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not recipe_history:
            print(f"{Fore.YELLOW}No recipes evaluated yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Recipe Evaluation History:{Style.RESET_ALL}")
            for idx, (text, polarity, rating_type) in enumerate(recipe_history, start=1):
                # Choose color & emoji based on rating
                if rating_type == "Five-Star":
                    color = Fore.GREEN
                    emoji = "🌟"
                elif rating_type == "Disaster":
                    color = Fore.RED
                    emoji = "🤢"
                else:
                    color = Fore.YELLOW
                    emoji = "🍲"

                print(f"{idx}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, {rating_type}{Style.RESET_ALL}")
        continue

    # Analyze sentiment / recipe review
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.2:
        rating_type = "Five-Star"
        color = Fore.GREEN
        emoji = "🌟"
    elif polarity < -0.2:
        rating_type = "Disaster"
        color = Fore.RED
        emoji = "🤢"
    else:
        rating_type = "Average"
        color = Fore.YELLOW
        emoji = "🍲"

    # Store in history
    recipe_history.append((user_input, polarity, rating_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {rating_type} rating detected! "
        f"Polarity: {polarity:.2f}{Style.RESET_ALL}")