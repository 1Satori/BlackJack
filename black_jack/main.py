#main file

import calculate_balance, check_amount, constants, new_logic, check_winner, DB

username = input(f'Hello, type your name: ')
amount = int(input("Type bet: "))
check_amount.check_amount(amount)
player = new_logic.result_player  #player score
croupier = new_logic.result_croupier  #croupier score


def start_game():
    new_logic.player()
    new_logic.croupier()
    calculate_balance.balance(player, croupier, amount)

start_game()