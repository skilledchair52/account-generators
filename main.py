# examples here right now
import os
import sys
import time

BANNER = """
   ░███                                                              ░██         ░██████                        
  ░██░██                                                             ░██        ░██   ░██                       
 ░██  ░██   ░███████   ░███████   ░███████  ░██    ░██ ░████████  ░████████    ░██         ░███████  ░████████  
░█████████ ░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██    ░██       ░██  █████ ░██    ░██ ░██    ░██ 
░██    ░██ ░██        ░██        ░██    ░██ ░██    ░██ ░██    ░██    ░██       ░██     ██ ░█████████ ░██    ░██ 
░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██ ░██   ░███ ░██    ░██    ░██        ░██  ░███ ░██        ░██    ░██ 
░██    ░██  ░███████   ░███████   ░███████   ░█████░██ ░██    ░██     ░████      ░█████░█  ░███████  ░██    ░██ 
"""

GENERATORS = {
    "1": {
        "name": "vibegames.com",
        "file": "vibegames.py",
    },
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    print(BANNER)
    print("═══════════════════════════════════════════")

def show_menu():
    print("\nOPTIONS:")
    for key, gen in GENERATORS.items():
        print(f"  [{key}] {gen['name']}")
    print("  [0] Exit")
    print("  [?] Help")

def show_help():
    clear_screen()
    show_header()
    print("\nHELP:")
    print("  • Pick a number to run that generator")
    print("  • Press 0 to quit")
    print("  • Press ? for this menu")
    input("\nPress Enter to continue...")

def run_generator(key):
    gen = GENERATORS[key]
    clear_screen()
    show_header()
    print(f"\n→ Starting {gen['name']}...")

    if os.path.exists(gen['file']):
        print(f"✓ Found {gen['file']}")
        print("─" * 40)
        time.sleep(1)

        try:
            with open(gen['file'], 'r') as f:
                exec(f.read())
        except Exception as e:
            print(f"✗ Error: {e}")
    else:
        print(f"✗ File {gen['file']} not found!")

    input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        show_header()
        show_menu()

        choice = input("\n> ").strip().lower()

        if choice == '0':
            print("\nBye!")
            sys.exit(0)
        elif choice == '?':
            show_help()
        elif choice in GENERATORS:
            run_generator(choice)
        else:
            input("Invalid option. Press Enter...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBye!")
        sys.exit(0)
