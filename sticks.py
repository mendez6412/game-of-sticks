from sticks_ai import AI

def is_pvp_game_over(players):
    response = input("Do you want to play again? [Y]es or [N]o: ").upper()
    if response not in ['Y', 'N']:
        is_pvp_game_over(players)
    if response == 'Y':
        pvp_main(players)
    else:
        exit(0)

def is_pva_game_over(computer, total_sticks, players):
    response = input("Do you want to play again? [Y]es or [N]o: ").upper()
    if response not in ['Y', 'N']:
        is_pva_game_over(players)
    if response == 'Y':
        pva_main(computer, total_sticks, players)
    else:
        exit(0)

def take_sticks():
    take = input("How many sticks do you want (1, 2, 3): ")
    try:
        take = int(take)
    except ValueError:
        print("Please enter a number from: 1, 2, 3")
        return take_sticks()
    if take < 1 or take > 3:
        print("Please enter a number from: 1, 2, 3")
        return take_sticks()
    return take

def humans_or_computer():
    friends = input("Do you want to play with [F]riends or the [C]omputer: ").upper()
    if friends in ['F', 'C']:
        if friends == 'F':
            return ["Player 1", "Player 2"]
        else:
            return ["You, the Human", 'Computer']
    else:
        print("Invalid input, please only enter F or C...")
        return humans_or_computer()

def is_input_valid(user_input):
    try:
        number = int(user_input)
        if number < 10 or number > 100:
            return False
        return number
    except:
        return False

def get_total_sticks():
    number = input("How many sticks do you want to start with, between 10 and 100: ")
    if is_input_valid(number):
        return is_input_valid(number)
    else:
        get_total_sticks()

def pvp_main(players):
    total_sticks = get_total_sticks()
    pvp_engine(total_sticks, players)

def pvp_engine(total_sticks, players):
    remaining_sticks = total_sticks
    while remaining_sticks >= 1:
        print("Sticks on the table: ", remaining_sticks)
        print(players[0], "'s turn")
        remaining_sticks -= take_sticks()
        if remaining_sticks <= 0:
            print("You lose, ", players[0])
            break
        players = players[::-1]
    is_pvp_game_over(players)

def pva_main(computer, total_sticks, players):
    pva_engine(computer, total_sticks, players)

def pva_engine(computer, total_sticks, players):
    remaining_sticks = total_sticks
    print("here")
    print(type(computer))
    while remaining_sticks >= 1:
        print("Sticks on the table: ", remaining_sticks)
        print(players[0], "'s turn")
        if players[0] == 'Computer':
            remaining_sticks -= computer.comp_turn(remaining_sticks)
        if players[0] == 'You, the Human':
            remaining_sticks -= take_sticks()
        if remaining_sticks <= 0:
            print("You lose, ", players[0])
            if players[0] == 'Computer':
                computer.learn_after_lose()
            elif players[0] == 'You, the Human':
                computer.learn_after_win()
            break
        players = players[::-1]
    is_pva_game_over(computer, total_sticks, players)

def main():
    print("Welcome...")
    total_sticks = get_total_sticks()
    computer = AI(total_sticks)
    players = humans_or_computer()
    if players[1] != 'Computer':
        pvp_main(players)
    else:
        pva_main(computer, total_sticks, players)

if __name__ == "__main__":
    main()
