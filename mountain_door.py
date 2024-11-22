import pydirectinput
import time


title_art = '''  __  __                   _        _         ____                   
|  \/  | ___  _   _ _ __ | |_ __ _(_)_ __   |  _ \  ___   ___  _ __ 
| |\/| |/ _ \| | | | '_ \| __/ _` | | '_ \  | | | |/ _ \ / _ \| '__|
| |  | | (_) | |_| | | | | || (_| | | | | | | |_| | (_) | (_) | |   
|_| _|_|\___/ \__,_|_| |_|\__\__,_|_|_| |_| |____/ \___/ \___/|_|   
| |/ /___ _   _                                                     
| ' // _ \ | | |                                                    
| . \  __/ |_| |                                                    
|_|\_\___|\__, |                                                    
          |___/                                                     '''

# Input sequence
sequence = [
    "Up", "Left", "Down", "Left", "Up", "Left", "Down", "Left", "Up", "Right",
    "Up", "Right", "Up", "Left", "Up", "Right", "Down", "Right", "Up", "Left",
    "Up", "Left", "Up", "Right", "Up", "Left", "Down", "Left", "Up", "Right",
    "Up", "Up", "Left", "Up", "Right", "Down", "Right", "Down", "Right", "Up",
    "Right", "Down", "Left", "Down", "Right", "Up", "Right", "Right", "Down",
    "Right", "Up", "Right", "Down", "Right", "Up", "Right", "Right", "Down",
    "Left", "Down", "Left", "Down", "Right", "Down", "Right", "Down", "Left",
    "Left", "Down", "Right", "Down", "Left", "Down", "Right", "Up", "Right",
    "Down", "Right", "Up", "Right", "Right", "Down", "Down", "Left", "Up",
    "Right", "Up", "Left", "Down", "Left", "Up", "Left", "Up", "Left", "Up",
    "Right", "Right", "Up", "Left", "Up"
]
 
# Mapping dictionary
mapping = {
    "Up": 'up',
    "Down": 'down',
    "Left": 'left',
    "Right": 'right'
}

# Convert the sequence to the corresponding list of characters
char_sequence = [mapping[direction] for direction in sequence]

print(title_art)

# Countdown timer before starting
def countdown(seconds):
    print(f"Starting in {seconds} seconds...")
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Go!")

# Sleep long enough for you to alt tab into the game
countdown(5)

# Start pressing buttons in sequence with feedback
for idx, key in enumerate(char_sequence):
    print(f"Pressing: {key}")  # Show which key is being pressed
    pydirectinput.press(key)
    time.sleep(0.1)  # Delay between key presses

print("\nSequence finished!")  # Notify user when sequence is complete
