party_level = 12  # Party's power level threshold
explored_dungeons = []  # List to store entered dungeons and their levels

while True:
    # Get dungeon name from the user
    dungeon_name = input("Enter the dungeon name: ").strip()
    
    # Get dungeon level and validate input
    while True:
        try:
            dungeon_level = int(input("Enter the dungeon level: ").strip())  # Convert input to integer
            if dungeon_level > 0:  # Ensure dungeon level is a positive integer
                break  # Exit loop if input is valid
            else:
                print("Invalid input. Dungeon level must be a positive integer.")  # Error message for non-positive numbers
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Error message for non-integer input
    
    # Store dungeon details as a pair of values (name, level)
    explored_dungeons.append((dungeon_name, dungeon_level))
    
    # Stop when reaching the final dungeon "Delfino Square", case insensitive
    if dungeon_name.lower() == "delfino square":
        break

# Display results for each entered dungeon
for name, level in explored_dungeons:
    if level <= party_level:
        print(f"We can freely explore {name}.")  # Message for accessible dungeons
    else:
        print(f"We cannot freely explore {name}.")  # Message for dungeons beyond party capability