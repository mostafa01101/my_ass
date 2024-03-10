# Game Name : Number Scrabble

# Purpose : There is a list of numbers from (1 to 9).The game begins by making the first
# player choose a number from the list, and then the second player chooses another number
# from the list. the turn continues until any of them reaches three numbers whose sum is 15.

# Name : Mustafa Mohamed Essa

# ID : 20230404

# Function to check if a combination of three numbers in the list adds up to 15
def check(the_list):
    for i in range(0, len(the_list)):
        for x in range(i+1, len(the_list)):
            for k in range(x+1, len(the_list)):
                if int(the_list[i]) + int(the_list[x]) + int(the_list[k]) == 15:
                    return True
    return False

# Initial list of numbers from 1 to 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lists to track the numbers picked by each player
player_one_list = []
player_two_list = []

# Variable to track if the game has ended
game_end = False

# Main game loop
while len(numbers) > 0 and not game_end:
    # Player one's turn
    while True:
         try:
           p1 = int(input("Player one: Enter your number "))
         except:
            print("please enter an integer")
            continue

         if p1 in numbers:
            player_one_list.append(p1)
            numbers.remove(p1)
            break
         else:
            print("Invalid choice. Choose again.")
         if len(numbers)==0:
            print("it's draw")
            break
    # Check if player one has won
    if check(player_one_list):
        print("Player one wins!")
        game_end = True
        break

    # Player two's turn
    while True:
         try:
           p2 = int(input("Player two: Enter your number "))
         except:
              print("please enter a integer")
              continue


         if p2 in numbers:
            player_two_list.append(p2)
            numbers.remove(p2)
            break
         else:
            print("Invalid choice. Choose again.")
         if len(numbers)==0:
            print("it's draw")
            break

    # Check if player two has won
    if check(player_two_list):
        print("Player two wins!")
        game_end = True
        break

# If the game ends without a winner, it's a draw
if not game_end:
    print("It's a draw! No player got exactly 15.")
