def update_win_loss_record():
    try:
        # Prompt the user to choose the ladder to update
        ladder_choice = input("Are you updating the 'guys' or 'girls' ladder? ").strip().lower()

        # Determine the correct file based on the choice
        if ladder_choice == "guys":
            filename = "s25_guys_ladder.txt"
        elif ladder_choice == "girls":
            filename = "s25_girls_ladder.txt"
        else:
            print("Invalid choice. Please enter 'guys' or 'girls'.")
            return

        # Prompt the user for the match result input string
        input_string = input("Enter the match result in the format 'FirstName LastName d. FirstName LastName': ").strip()

        # Parse the input string
        if " d. " not in input_string:
            print("Invalid input format. Use 'FirstName LastName d. FirstName LastName'.")
            return
        
        # Split the input string into winner and loser
        parts = input_string.split(" d. ")
        if len(parts) != 2:
            print("Invalid input format. Use 'FirstName LastName d. FirstName LastName'.")
            return
        
        winner = parts[0].strip()
        loser = parts[1].strip()

        # Read and parse the existing records
        players = {}
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 4:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                firstname, lastname, wins, losses = parts
                full_name = f"{firstname} {lastname}"
                players[full_name] = [int(wins), int(losses)]
        
        # Check if winner and loser exist in the file
        if winner not in players:
            print(f"Winner '{winner}' not found in the file.")
            return
        if loser not in players:
            print(f"Loser '{loser}' not found in the file.")
            return

        # Update the win-loss records
        players[winner][0] += 1  # Increment winner's wins
        players[loser][1] += 1   # Increment loser's losses

        # Write the updated records back to the file
        with open(filename, 'w') as file:
            for name, record in players.items():
                firstname, lastname = name.split()
                file.write(f"{firstname} {lastname} {record[0]} {record[1]}\n")

        print(f"Win-loss record updated successfully for: {input_string}")

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def swap_positions():
    try:
        # Prompt the user to choose the ladder to update
        ladder_choice = input("Are you swapping on the 'guys' or 'girls' ladder? ").strip().lower()

        # Determine the correct file based on the choice
        if ladder_choice == "guys":
            filename = "s25_guys_ladder.txt"
        elif ladder_choice == "girls":
            filename = "s25_girls_ladder.txt"
        else:
            print("Invalid choice. Please enter 'guys' or 'girls'.")
            return

        # Prompt the user for the two names to swap
        input_string = input("Enter the two names to swap in the format 'FirstName LastName :: FirstName LastName': ").strip()

        # Parse the input string
        if " :: " not in input_string:
            print("Invalid input format. Use 'FirstName LastName :: FirstName LastName'.")
            return
        
        parts = input_string.split(" :: ")
        if len(parts) != 2:
            print("Invalid input format. Use 'FirstName LastName :: FirstName LastName'.")
            return
        
        name1 = parts[0].strip()
        name2 = parts[1].strip()

        # Read the existing ladder
        with open(filename, 'r') as file:
            ladder = file.readlines()

        # Find the indices of the two players
        index1, index2 = -1, -1
        for i, line in enumerate(ladder):
            if line.startswith(name1):
                index1 = i
            if line.startswith(name2):
                index2 = i

        if index1 == -1:
            print(f"Player '{name1}' not found in the file.")
            return
        if index2 == -1:
            print(f"Player '{name2}' not found in the file.")
            return

        # Swap the positions in the ladder
        ladder[index1], ladder[index2] = ladder[index2], ladder[index1]

        # Write the updated ladder back to the file
        with open(filename, 'w') as file:
            file.writelines(ladder)

        print(f"Players '{name1}' and '{name2}' swapped successfully.")

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Program menu 
    while True:
        print("\nSelect an Option:")
        print("1. Update Win Loss Records")
        print("2. Swap Two People on the Ladder")
        print("3. Exit Program")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            update_win_loss_record()
        elif choice == "2":
            swap_positions()
        elif choice == "3":
            print("Program Exit")
            break # End
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
