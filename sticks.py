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
        is_pva_game_over(computer, total_sticks, players)
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
    friends = input("Do you want to play with [F]riends or the [C]omputer or the [S]uperComputer: ").upper()
    if friends in ['F', 'C', 'S']:
        if friends == 'F':
            return ["Player 1", "Player 2"]
        elif friends == 'C':
            return ["You, the Human", 'Computer']
        else:
            return ['Computer1', 'Computer2']
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

def pvp_main(total_sticks, players):
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

def training_engine(computer, computer2, total_sticks, players):
    remaining_sticks = total_sticks
    while remaining_sticks >= 1:
        if players[0] == 'Computer1':
            remaining_sticks -= computer.comp_turn(remaining_sticks)
        if players[0] == 'Computer2':
            remaining_sticks -= computer2.comp_turn(remaining_sticks)
        if remaining_sticks <= 0:
            if players[0] == 'Computer2':
                computer.learn_after_lose()
            elif players[0] == 'Computer1':
                computer.learn_after_win()
            break
        players = players[::-1]

def loading(simulations_remaining):
    if simulations_remaining == 95000:
        print("Please wait as we simulate an epic duel...")
    elif simulations_remaining == 90000:
        print("Don't Panic... in large, friendly letters")
    elif simulations_remaining == 80000:
        print("I promise, we're almost there...")
    elif simulations_remaining == 50000:
        print("Oops, I have to start over...")
    elif simulations_remaining == 45000:
        print("I may not have gone where I intended to go, ")
    elif simulations_remaining == 35000:
        print("but I think I've ended up where I needed to be.")
    elif simulations_remaining == 25000:
        print("Sub-Sampling Water Data")
    elif simulations_remaining == 15000:
        print("Prioritizing Landmarks")
    elif simulations_remaining == 4000:
        print("4")
    elif simulations_remaining == 3000:
        print("3")
    elif simulations_remaining == 2000:
        print("2")
    elif simulations_remaining == 1000:
        print("1")
    elif simulations_remaining == 10:
        print("phew...")

def main():
    print("Welcome to Sticks! Don't pick up the last stick! Sticks!")
    total_sticks = get_total_sticks()
    computer = AI(total_sticks)
    computer2 = AI(total_sticks)
    players = humans_or_computer()
    if players[1] == 'Player 2':
        pvp_main(total_sticks, players)
    if players[0] == 'Computer1' and players[1] == 'Computer2':
        print("Please wait while the computer duels it out... imagine Transformers or something")
        simulations_remaining = 100000
        while simulations_remaining > 0:
            loading(simulations_remaining)
            training_engine(computer, computer2, total_sticks, players)
            simulations_remaining -= 1
        players = ['You, the Human', "Computer"]
        pva_main(computer, total_sticks, players)
    else:
        pva_main(computer, total_sticks, players)

if __name__ == "__main__":
    main()
