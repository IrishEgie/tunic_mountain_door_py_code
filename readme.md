# Mountain Door Solution Script - Tunic

This tool automates a sequence of key presses using the `pydirectinput` library, designed for simulating button presses for the **Tunic Golden Path Mountain Door** at the end of the game. Enjoy automating your gameplay!

![Tunic Mountain Door](tunic-mountain-door.jpg)

## Features
- **Key Press Automation**: Automatically simulates a series of key presses.
- **Countdown Timer**: Waits for 5 seconds before starting the sequence, allowing you to alt-tab into your game or app.
- **Real-Time Feedback**: Displays which key is being pressed at the moment.
- **Completion Notification**: Shows a message when the entire sequence is completed.
- **Command Prompt Output**: Keeps the console open to show real-time feedback during execution.

## Requirements
- Must have collected all but one of the manual pages. Otherwise script wont work. 

## Usage

1. **Download the Executable**: Download the `mountain_door.exe` file from the release.
2. **Run the Executable**: Simply double-click on the `mountain_door.exe` to start.
   - A **5-second countdown** will begin, allowing you time to alt-tab into your game or app where the key presses will be simulated.
   - The console will display real-time feedback, showing which key is being pressed.
   - Once the sequence is complete, you will see a **"Sequence finished!"** message in the console.

### Running via Batch File
To ensure that the Command Prompt stays open while running the `.exe` file, you can use the included `.bat` file:
1. **Download the `run_with_console.bat`** file.
2. **Run the Batch File**: Double-click the batch file to open the executable with the Command Prompt window visible.

This allows you to see all console output during the execution.

### Example Command (for advanced users):
If you prefer running the executable from the Command Prompt manually:
```bash
mountain_door.exe
```
