import random
result_player = []
result_croupier = []
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 #all cards in deck


def player():
    score = random.choice(deck) + random.choice(deck)
    if score > 21:
        result_player.append(0)
        print(f'You have {score}, too much')
    if score == 21:
        result_player.append(21)
        print(f'You have {score}')
    if score < 21:
        print(f'You have {score}, take more? (Y/N)')
    answer = input()
    if answer == "Y" or answer == "N":
        if answer == "Y":
            score += random.choice(deck)
            print(f'You have {score}')
            if score <= 21:
                result_player.append(score)
        if answer == "N":
            result_player.append(score)
            print(f'You have {score}')
    else:
        print(f'Uncorrect answer, choose Y or N')
        exit()


def croupier():
    score = random.choice(deck) + random.choice(deck)
    if score > 21:
        result_croupier.append(0)
        print(f'Croupier have {score}')
    if score == 21:
        result_croupier.append(21)
        print(f'Croupier have 21')
    if score <= 12:
        score += random.choice(deck)
        print(f'Croupier have {score}')
        if score > 21:
            result_croupier.append(0)
        if score <= 21:
            result_croupier.append(score)
    else:
        result_croupier.append(score)
        print(f'Croupier have {score}')






