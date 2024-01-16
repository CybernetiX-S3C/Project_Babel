import time
import random
import platform
import os
import threading
import tkinter as tk
from tkinter import messagebox

# Function to create system overload effects
def overload_protocol():
    while True:
        # Change desktop wallpaper rapidly (platform-specific implementations)
        if platform.system() == "Windows":
            wallpaper_path = "C:\\Windows\\Wallpapers\\"  # Windows default wallpaper path
            os.system(f"rundll32.exe user32.dll,UpdatePerUserSystemParameters 1, {os.path.join(wallpaper_path, random.choice(os.listdir(wallpaper_path)))}")
        elif platform.system() == "Darwin":  # macOS
            wallpaper_path = "/Library/Desktop Pictures/"  # macOS default wallpaper path
            os.system(f"osascript -e 'tell application \"System Events\" to set picture of every desktop to \"{os.path.join(wallpaper_path, random.choice(os.listdir(wallpaper_path)))}\"'")
        else:  # Linux (using gsettings for GNOME)
            wallpaper_path = "/usr/share/backgrounds/"  # Linux default wallpaper path
            os.system(f"gsettings set org.gnome.desktop.background picture-uri file:///{os.path.join(wallpaper_path, random.choice(os.listdir(wallpaper_path)))}")

        time.sleep(0.5)

        # Open random folders (platform-specific implementations)
        if platform.system() == "Windows":
            os.system("start explorer some_random_folder")
        elif platform.system() == "Darwin":
            os.system("open -R /path/to/random/folder")
        else:
            os.system("xdg-open /path/to/random/folder")

        # Display fake error messages
        error_message = "Critical System Malfunction! *Beep* *Boop* *Bzzt*"
        message_box = tk.Tk()
        message_box.withdraw()  # Hide main window
        messagebox.showerror("Babel Protocol Activated", error_message)

# Function to create and move a cyber pet
def cyber_guardian():
    # Create a pixelated pet using ASCII art or a graphics library
    pet = "(^_^)"
    pet_x = random.randint(1, 80)
    pet_y = random.randint(1, 25)

    while True:
        # Clear previous pet position
        print("\033[F\033[K" * 5, end="")  # Move cursor up and clear lines

        # Move pet randomly and display
        new_x = pet_x + random.randint(-2, 2)
        new_y = pet_y + random.randint(-1, 1)
        if 0 < new_x < 80 and 0 < new_y < 24:
            pet_x = new_x
            pet_y = new_y
        print("\033[{};{}H{} {}".format(pet_y + 1, pet_x + 1, pet, random.choice(["Strengthen your passwords!", "Beware of suspicious links!", "Back up data regularly!"])))
        time.sleep(0.1)

# Function for interactive cybersecurity challenges
def security_tests():
    # Present a series of challenges (replace with your own)
    challenges = [
        ("Decrypt the message: What's the first rule of cybersecurity?", "Never reveal your password"),
        ("Identify the phishing attempt: Which link is suspicious?", "https://freegiftz.com/claim-prize"),
        ("Evaluate password strength: hunter2", "Made of paper")
    ]

    for question, answer in challenges:
        user_response = input(question + "\n").lower()
        if user_response == answer.lower():
            print("Correct! You've passed the test.")
        else:
            print("Incorrect. Remember,", answer + ".")

# Main prank function - Activate all features and terminate after a set duration
def babel_protocol():
    print("WARNING: Babel Protocol Engaged!")
    time.sleep(1)

    # Launch all effects as concurrent threads
    overload_thread = threading.Thread(target=overload_protocol)
    pet_thread = threading.Thread(target=cyber_guardian)
    test_thread = threading.Thread(target=security_tests)
