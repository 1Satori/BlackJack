def check_amount(amount):
    if amount < 500 or amount > 50000:
        print(f'Uncorrected bet, minimal bet - 500, maximum - 50000')
        exit()
    return amount