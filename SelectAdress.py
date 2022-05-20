import bitcoin_balance_checker


def Sel():
    word = 'Public Address 1: '  # Искомое слово
    dorw = 'Public Address 1 compressed: '  # Искомое слово 2
    Lstt = []
    f = open('file_wall.txt', 'r')
    for line in f:
        if word in line:
            text = str(line)
            #List.append(text.partition(word)[2])

            arq1 = open('addresses-with-balance-yay.txt', 'a')
            address = str.strip(text.partition(word)[2])
            #print(address)
            bitcoin_balance_checker.check_balance(address)

        if dorw in line:
            text = str(line)
            #List.append(text.partition(dorw)[2])

            arq1 = open('addresses-with-balance-yay.txt', 'a')
            address = str.strip(text.partition(dorw)[2])
            #print(address)
            bitcoin_balance_checker.check_balance(address)


