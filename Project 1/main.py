from textblob import TextBlob
from colorama import init, Fore
import time
import re

# Initialize colorama
init(autoreset=True)

# Global storage
history = []
sentiment_summary = {"positive": 0, "negative": 0, "neutral": 0}

def show_processing_animation():
    print("\nAnalyzing", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment, polarity

def execute_command(command):
    if command == "summary":
        print("\n--- Sentiment Summary ---")
        for k, v in sentiment_summary.items():
            print(f"{k.capitalize()}: {v}")
    elif command == "reset":
        history.clear()
        for k in sentiment_summary:
            sentiment_summary[k] = 0
        print(Fore.CYAN + "Data reset successfully.")
    elif command == "history":
        print("\n--- Conversation History ---")
        for i, (msg, sentiment, polarity) in enumerate(history, 1):
            print(f"{i}. [{sentiment.capitalize()} | {polarity:.2f}]: {msg}")
    elif command == "help":
        print("\nAvailable commands: summary, reset, history, help, exit")
    else:
        print(Fore.YELLOW + "Unknown command. Type 'help' for a list of commands.")

def get_valid_name():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            return name
        print("Name should only contain alphabetic characters.")

def print_colored_feedback(sentiment, polarity):
    if sentiment == "positive":
        color = Fore.GREEN
    elif sentiment == "negative":
        color = Fore.RED
    else:
        color = Fore.YELLOW
    print(color + f"Sentiment: {sentiment.capitalize()} (Polarity: {polarity:.2f})")

def save_summary_to_file(username):
    filename = f"{username}_sentiment_analysis.txt"
    with open(filename, "w") as f:
        f.write("--- Sentiment Analysis Summary ---\n")
        for k, v in sentiment_summary.items():
            f.write(f"{k.capitalize()}: {v}\n")
        f.write("\n--- Conversation History ---\n")
        for i, (msg, sentiment, polarity) in enumerate(history, 1):
            f.write(f"{i}. [{sentiment.capitalize()} | {polarity:.2f}]: {msg}\n")
    print(Fore.CYAN + f"Summary saved to {filename}")

# Main Chatbot Loop
print("Welcome to the Spy-Themed Sentiment Analyzer Bot!")
user_name = get_valid_name()
print(f"Hello, {user_name}! Type any sentence to analyze its sentiment.")
print("Type 'help' for a list of commands.")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        break
    elif user_input.lower() in ["summary", "reset", "history", "help"]:
        execute_command(user_input.lower())
    else:
        show_processing_animation()
        sentiment, polarity = analyze_sentiment(user_input)
        sentiment_summary[sentiment] += 1
        history.append((user_input, sentiment, polarity))
        print_colored_feedback(sentiment, polarity)

# Final Report
print("\nThank you for using the bot. Here's your final report:")
execute_command("summary")
save_summary_to_file(user_name)
