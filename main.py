import random

choices = {
    1:"Rock",
    2:"Scissor",
    3:"Paper"
}

# diciding feature when user won
beats = {
    1: 2,   # Rock beats Scissor
    2: 3,   # Scissor beats Paper
    3: 1    # Paper beats Rock
}

# funtion to check input
def check_input(prompt, max_val = 3, min_val = 1, allow_quit = False):
    while True:
        value = input(prompt)

        if allow_quit and value.lower() == "q":
            return "q"

        try:
            num = int(value)
            if min_val <= num <= max_val:
                return num
            else:
                print("Invalid input! Please enter a value between", min_val, "and", max_val)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# funtion to end game
def game_end():
    print("Do you want to play again a fresh game😼\n1. Yes\n2. No")
    user_choice = check_input("Enter your choice:", max_val = 2)
    if user_choice == 1:
      return True
    else:
      print("==============================\n     Thanks for playing❤️\n     Visit and play again🥺\n==============================")
      return False

def result_print(bot_won, user_won, tie_match):
    total_game = (bot_won + user_won + tie_match)
    print("Total matches played:", total_game)
    print("You won:", user_won )
    print("Bot won:", bot_won)
    print("Matches tied:", tie_match)
    if tie_match < bot_won > user_won:
        print("Better luck next time☺️, this time bot won")
    elif tie_match < user_won > bot_won:
        print("Congratulations❤️, You won the game ")
    else:
        print("Its a tie🥲  Try again😁")

# funtion to retry the game
def play_again(bot_won, user_won, tie_match):
    print("Do you want a rematch with the bot and check who will win this time \n1. Yes \n2. No, show the end result")
    retry_choise = check_input("Enter your choice:", max_val= 2)
    if retry_choise == 1:
        return False
    else:
        result_print(bot_won, user_won, tie_match)
        return True

# funtion for game run
def game_run(bot_won, user_won, tie_match):
    print('Welcome❤️. Bot has selected his answer now its your turn to select your choice. \nEnter digits that are assigned to your choice or if you want to quit the game enter "q/Q"')
    print("1. Rock \n2. Scissor \n3. Paper")

    bot_choice = random.randint(1, 3)
    user_choice = check_input("Enter your choice:", allow_quit = True)

    if user_choice == "q":
        result_print(bot_won, user_won, tie_match)

    elif bot_choice == user_choice:
        print("Its a tie \nBot choose :", choices[bot_choice])
        tie_match += 1

    elif bot_choice == beats[user_choice]:
        print("Congratulations❤️, You won \nBot choose :", choices[bot_choice])
        user_won += 1

    else:
        print("Bot won! Better luck next time\nBot choose :", choices[bot_choice])
        bot_won += 1

    return bot_won, user_won, tie_match

# funtion for convineint
def run_main():
    bot_won = 0
    user_won = 0
    tie_match = 0

    while True:
        bot_won, user_won, tie_match = game_run(bot_won, user_won, tie_match)

        if play_again(bot_won, user_won, tie_match):
            return True

# result of best of 5 mode
def result_bestof5mode(bot_won, user_won, tie_match):
    total_match = (bot_won + user_won + tie_match)

    if user_won == 3:
        result_print(bot_won, user_won, tie_match)
        return True

    elif bot_won == 3:
        result_print(bot_won, user_won, tie_match)
        return True

    elif total_match == 5:
        result_print(bot_won, user_won, tie_match)
        return True

    else:
        return False

# for best of 5 mode
def best_of_5_mode():
    bot_won = 0
    user_won = 0
    tie_match = 0

    while True:
        bot_won, user_won, tie_match = game_run(bot_won, user_won, tie_match)

        if result_bestof5mode(bot_won, user_won, tie_match):
            return True


# funtion to show rules
def show_rules():
    print ("==============================\nGAME RULES\n \n🎮 Objective\nDefeat the computer by choosing the correct move.\n \n📌 Choices\n \n1. Rock 🪨\n2. Scissor ✂️\n3. Paper 📄\n \n🏆 Winning Rules\n• Rock beats Scissor.\n• Scissor beats Paper.\n• Paper beats Rock.\n \n🤖 How to Play\n \n1. Choose one of the three options.\n2. The computer will randomly choose its move.\n3. The winner is decided according to the game rules.\n4. You can play multiple rounds and view your score.\n \n⭐ Best of 5 Mode\n• The match continues until:\n \n* You win 3 rounds, OR\n* The Bot wins 3 rounds, OR\n* 5 total rounds are completed.\n* Final statistics will be displayed automatically.\n \n📊 Statistics \nAt the end of the match you can see:\n• Total Matches Played\n• Your Wins\n• Bot Wins\n• Draw Matches\n⌨️ Controls\n• Enter:\n1 = Rock\n2 = Scissor\n3 = Paper\n• Enter Q (or q) anytime during gameplay to quit the current match.\n \n🎯 Have Fun and Try to Beat the Bot!\n \n==============================\nBest of Luck! ❤️")
    print("")
    print("Select the appropriate option:-\n1. Play (if you want to play the game) \n2. Exit the game ")
    your_chose = check_input("Enter your choice", max_val = 2)
    if your_chose == 1:
        return main_screen()
    else:
        print("Thanks, Visit us again😌")
        return False

# function for calling main screen
def main_screen():
    print("==============================\n Rock Paper Scissor \n============================== \n \n1. Start Game(Normal Mode) \n2. Best of 5 mode \n3. Rules \n4. Exit")
    choice = check_input("Enter Choice:", max_val = 4)
    if choice == 1:
        return run_main()

    elif choice == 2:
        return best_of_5_mode()

    elif choice == 3:
        return show_rules()

    else:
        print("Thanks for playing. \nGoodbye👋🏻 Visit again")
        return False

# calling to intiate our code
while True:

    if not main_screen():
        break

    if not game_end():
        break
