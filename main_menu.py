#!/usr/bin/env python3
"""
Main Menu for Python Learning Projects
This menu allows you to run different Python exercises and games.
"""

import os
import subprocess
import sys

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Display the main menu options"""
    clear_screen()
    print("=" * 50)
    print("🐍 PYTHON LEARNING PROJECTS 🐍")
    print("=" * 50)
    print()
    print("Available Programs:")
    print("1. 📝 Day 1 - Band Name Generator")
    print("2. 📊 Day 2 - Data Types")
    print("3. 🎯 Day 3 - Conditions")
    print("4. 🎲 Day 4 - Random & Modules")
    print("5. 🔄 Day 5 - Loops")
    print("6. 🔧 Day 6 - Functions")
    print("7. 🎮 Day 7 - Hangman Game")
    print("8. 🔐 Day 8 - Caesar Cipher")
    print("9. 📚 Day 9 - Dictionaries")
    print("10. ⚡ Day 10 - Return Functions")
    print("11. 🏆 Secret Auction")
    print("0. ❌ Exit")
    print()
    print("=" * 50)

def run_program(choice):
    """Run the selected program"""
    programs = {
        1: ("Day_1/print_input_day_1.py", "Day 1 - Band Name Generator"),
        2: ("Day_2/DataTypes_day_2.py", "Day 2 - Data Types"),
        3: ("Day_3/Condition_day_3.py", "Day 3 - Conditions"),
        4: ("Day_4/Random_ Day_4.py", "Day 4 - Random & Modules"),
        5: ("Day_5/Loops_Day_5.py", "Day 5 - Loops"),
        6: ("Day_6/Day_6_Function.py", "Day 6 - Functions"),
        7: ("hangman_7/Day_7_Hangman.py", "Day 7 - Hangman Game"),
        8: ("Caesar Cipher/main.py", "Day 8 - Caesar Cipher"),
        9: ("Day_9_Dictionaries/main.py", "Day 9 - Dictionaries"),
        10: ("Day_10_Return_Function/main.py", "Day 10 - Return Functions"),
        11: ("auction/main.py", "Secret Auction"),
    }
    
    if choice in programs:
        program_path, program_name = programs[choice]
        if os.path.exists(program_path):
            print(f"\n🚀 Starting {program_name}...")
            print("-" * 50)
            try:
                # Change to the program's directory and run it
                program_dir = os.path.dirname(program_path)
                program_file = os.path.basename(program_path)
                
                if program_dir:
                    original_dir = os.getcwd()
                    os.chdir(program_dir)
                    subprocess.run([sys.executable, program_file])
                    os.chdir(original_dir)
                else:
                    subprocess.run([sys.executable, program_path])
                    
            except KeyboardInterrupt:
                print("\n\n⚠️  Program interrupted by user")
            except Exception as e:
                print(f"\n❌ Error running program: {e}")
            
            input("\n📋 Press Enter to return to main menu...")
        else:
            print(f"❌ Program file not found: {program_path}")
            input("📋 Press Enter to continue...")
    else:
        print("❌ Invalid selection!")
        input("📋 Press Enter to continue...")

def main():
    """Main menu loop"""
    while True:
        display_menu()
        
        try:
            choice = input("👉 Select a program (0-11): ")
            
            if choice == '0':
                clear_screen()
                print("👋 Thanks for using Python Learning Projects!")
                print("Happy coding! 🚀")
                break
            
            choice_num = int(choice)
            if 1 <= choice_num <= 11:
                run_program(choice_num)
            else:
                print("❌ Please enter a number between 0 and 11")
                input("📋 Press Enter to continue...")
                
        except ValueError:
            print("❌ Please enter a valid number")
            input("📋 Press Enter to continue...")
        except KeyboardInterrupt:
            clear_screen()
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()