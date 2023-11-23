import constants


def balance(player, croupier, amount):
    if player > croupier:
        constants.userbalans += amount
        print(f'You win, your balance is {constants.userbalans}')
    else:
        constants.userbalans -= amount
        print(f'You lose, your balance is {constants.userbalans}')



