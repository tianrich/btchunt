import random

with open("words.txt", "r") as f:
    bip39_words = f.read().splitlines()

while True:
    bip39_codes = []
    for i in range(12):
        bip39_codes.append(random.choice(bip39_words))
    # check the balance of the bip39 codes here (not implemented)
    balance = 0  # temporarily setting balance to 0
    if balance > 0:
        with open("found.txt", "a") as f:
            f.write(" ".join(bip39_codes) + "\n")
            print(f"Code with positive balance found: {' '.join(bip39_codes)} saved to found.txt")
    else:
        print(f"Code with zero balance generated: {' '.join(bip39_codes)}")
