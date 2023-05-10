from bit import *

import base58

import multiprocessing

def run_code():

    # Opening a txt file to write the results
    file = open("addresses_with_balance.txt", "a")

    addresses = set()

    while True:

        private_key = Key()

        wif = private_key.to_wif()

        address = private_key.address

        if address in addresses:

            continue

        addresses.add(address)

        balance = private_key.get_balance("satoshi")

        print("WIF: ", wif)
        print("Address: ", address)
        print("Balance: ", balance, "satoshis")

        try:
            decoded = base58.b58decode_check(address)

            if len(decoded) == 21 and decoded[0] in [0x00, 0x05]:
                valid = True
            else:
                valid = False

        except ValueError:
            valid = False

        if valid:

            if int(balance) > 0:

                # Writing the results to the txt file
                file.write("WIF: " + wif + "\n")
                file.write("Address: " + address + "\n")
                file.write("Balance: " + str(balance) + " satoshis\n")
                file.write("\n")

        else:

            print("Invalid address!")

    file.close()

num_processes = 4

if __name__ == '__main__':

    processes = []

    for i in range(num_processes):

        p = multiprocessing.Process(target=run_code)

        processes.append(p)

        p.start()

    for p in processes:
        p.join()
