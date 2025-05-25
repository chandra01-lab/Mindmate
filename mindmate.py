import datetime

def welcome():
    print("Welcome to MindMate 🌱")
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Let's check in with your mind today.")
    return name

def get_mood():
    moods = ["happy", "sad", "anxious", "angry", "neutral", "excited"]
    print("\nHow are you feeling today?")
    print("Options:", ", ".join(moods))
    mood = input("Your mood: ").lower()
    while mood not in moods:
        print("Invalid mood. Please choose from the list.")
        mood = input("Your mood: ").lower()
    return mood

def get_journal_entry():
    print("\nWould you like to write something about your day?")
    entry = input("Write here (or press Enter to skip): ")
    return entry

def save_entry(name, mood, entry):
    today = datetime.date.today()
    with open(f"{name}_mindmate_log.txt", "a") as file:
        file.write(f"{today} - Mood: {mood}\n")
        if entry:
            file.write(f"    Journal: {entry}\n")
        file.write("\n")

def main():
    name = welcome()
    mood = get_mood()
    journal = get_journal_entry()
    save_entry(name, mood, journal)
    print("\nThanks for checking in today! See you tomorrow. 🌞")

if __name__ == "__main__":
    main()
