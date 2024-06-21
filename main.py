import random
import time
import os

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Tool banner
tool_banner = """


88          88        88
88          88        88
88          88        88
88          88aaaaaaaa88
88          88********88
88          88        88
88          88        88
88888888888 88        88


 LH-742 - Automated Giveaway Winner Selector

            [ LocalHost.07 ]
"""

# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'

# Main function
def main():
    clear_screen()
    print(tool_banner)
    print(f"{GREEN}Enter the names of participants (separated by commas): {ENDC}")
    participants = input().split(',')
    participants = [name.strip() for name in participants]

    print(f"\n{GREEN}How many winners would you like to select? {ENDC}")
    num_winners = int(input())

    print(f"\n{GREEN}Selecting the winners...{ENDC}")
    time.sleep(1)

    # Animation progress bar
    progress_bar_length = 20
    for i in range(progress_bar_length):
        progress = "#" * (i + 1)
        print(f"\rSelecting... [{progress.ljust(progress_bar_length)}] {i + 1}/{progress_bar_length}", end="")
        time.sleep(0.1)

    print(f"\n\n{GREEN}And the winners are...{ENDC}")
    time.sleep(1)

    # Select the winners
    winners = random.sample(participants, num_winners)
    for i, winner in enumerate(winners, 1):
        print(f"{RED}** {winner} **{ENDC}")

    print(f"\n{GREEN}Press Enter to exit...{ENDC}")
    input()

if __name__ == "__main__":
    main()
