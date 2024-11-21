import pyautogui
import time

# Arrow sequence for the mountain door unlock
arrow_sequence = [
    "up", "left", "down", "left", "up", "left", "down", "left", "up", "right", "up", "right", 
    "up", "left", "up", "right", "down", "right", "up", "left", "up", "left", "up", "right", 
    "up", "left", "down", "left", "up", "right", "up", "up", "left", "up", "right", "down", 
    "right", "down", "right", "up", "right", "down", "left", "down", "right", "up", "right", 
    "right", "down", "right", "up", "right", "down", "right", "up", "right", "right", "down", 
    "left", "down", "left", "down", "right", "down", "right", "down", "left", "left", "down", 
    "right", "down", "left", "down", "right", "up", "right", "down", "right", "up", "right", 
    "right", "down", "down", "left", "up", "right", "up", "left", "down", "left", "up", "left", 
    "up", "left", "up", "right", "right", "up", "left", "up"
]

# Countdown before starting the sequence (gives you time to focus on the game)
print("Starting in 5 seconds...")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# Loop through each direction in the arrow sequence
for direction in arrow_sequence:
    print(f"Pressing {direction} arrow key")  # Feedback on the key being pressed
    pyautogui.press(direction)
    time.sleep(0.3)  # Adjusted to simulate more realistic speed, you can increase this if needed

print("Arrow sequence executed.")
